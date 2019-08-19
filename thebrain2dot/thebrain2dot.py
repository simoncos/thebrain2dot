import json
import codecs
import math

import networkx as nx
import pygraphviz


def brain_json2dot(thoughts_path, links_path, dot_path='thebrain.dot', png_path='thebrain.png',
                   layout='dot', bg_color='grey22', node_shape='circle', node_color='white',
                   edge_default_color='white', edge_splines='', edge_font_size=10):
                        
    G = _init_graph(bg_color=bg_color, node_shape=node_shape, node_color=node_color,
                    edge_splines=edge_splines, edge_font_size=edge_font_size)
    nodes_json, links_json, id2link_type = _read_thebrain_json(thoughts_path, links_path)
    G = _build_graph(G, nodes_json, links_json, id2link_type, edge_default_color)

    G.write(dot_path)
    print('Successfully generated "{}".'.format(dot_path))
    # neato, dot, twopi, circo, fdp, nop, wc, acyclic, gvpr, gvcolor, ccomps, sccmap, tred, sfdp, unflatten.
    G.layout(prog=layout)
    G.draw(png_path)
    print('Successfully generated "{}" with layout "{}".'.format(png_path, layout))


def _init_graph(bg_color, node_shape, node_color, edge_splines, edge_font_size):
    G = pygraphviz.AGraph(strict=False, directed=True, encoding='utf-8')
    G.graph_attr.update({
        'bgcolor': bg_color,
        'penwidth': 1,
        'splines': edge_splines,
        }
    )
    G.node_attr.update({
        'shape': node_shape,
        'fixedsize': True,
        'color': node_color,
        'fontcolor': node_color,
        #  'fillcolor': 'white',
        #  'style': 'filled',
        #  'width': 1.2,    
        }
    )
    G.edge_attr.update({
        'fontsize': edge_font_size,
        }
    )
    return G


def _read_thebrain_json(thoughts_path, links_path):
    nodes_json = {}
    for line in codecs.open(thoughts_path, 'r', 'utf-8-sig'):
        node = json.loads(line)
        nodes_json[node['Id']] = node.get('Name')

    links_json = []
    id2link_type = {}
    for line in codecs.open(links_path, 'r', 'utf-8-sig'):  
        link = json.loads(line)
        if link['Meaning'] != 0:
            links_json.append(link)
        else:
            id2link_type[link['Id']] = link

    return nodes_json, links_json, id2link_type


def _build_graph(G, nodes_json, links_json, id2link_type, edge_default_color):
    # Nodes (Thoughts)
    node2pr = _rank_thoughts(nodes_json, links_json)
    for node, pr in node2pr.items():
        # G.add_node(node, width=math.sqrt(150*pr))
        G.add_node(node, width=100*pr, fontsize=100*math.sqrt(5*pr))

    # Edges (Links)
    for e in links_json:
        typeId = e.get('TypeId')
        direction = e.get('Direction')

        label = ''
        color = edge_default_color

        link_type = id2link_type.get(typeId)
        if link_type:
            label = link_type['Name']
            if link_type.get('Color'):
                color = _rgb_int2hexstr(_thebrain_rgbint2rgbint(link_type['Color']))
            if direction == -1 and link_type.get('Direction'):
                direction = link_type['Direction']

        label = e.get('Name', label)
        color = e.get('Color', color)        
        if direction in [1, 5]:
            dirtype = 'forward'
        elif direction in [3, 7]:
            dirtype = 'back'
        else:
            dirtype = 'none'
        G.add_edge(str(nodes_json.get(e['ThoughtIdA'])), str(nodes_json.get(e['ThoughtIdB'])), 
            label=label, color=color, fontcolor=color, dir=dirtype)

    return G


def _rank_thoughts(nodes_json, links_json):
    G_nx = nx.Graph()
    G_nx.add_edges_from([(nodes_json.get(n['ThoughtIdA']), nodes_json.get(n['ThoughtIdB'])) for n in links_json])
    return nx.pagerank(G_nx, alpha=0.9)


def _rgb_int2hexstr(rgbint):
    rgbtuple = (rgbint // 256 // 256 % 256, rgbint // 256 % 256, rgbint % 256)
    return '#%02x%02x%02x' % rgbtuple


def _thebrain_rgbint2rgbint(thebrain_rgbint):
    return 256^3 + thebrain_rgbint
