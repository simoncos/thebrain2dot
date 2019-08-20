# thebrain2dot

TheBrain10 `.json` (File>Export>JSON Files 
) to `.dot` visualization with Graphviz

- Python 3 support
- UTF-8 support
- Nodes (`thoughts.json`)
    - support shapes, colors
    - size depends on PageRank centrality
- Links (`links.json`)
    - support types, directions, colors
- Layout
    - support layout (algorithm), splines

Before:

![](test/thebrain_screenshot.png)

After:

![](test/thebrain.png)

More Complicated Example:

![](test/thebrain_complex.PNG)

## API

Example: see [test/test.py](test/test.py)

```python
brain_json2dot(thoughts_path, links_path, dot_path='thebrain.dot', png_path='thebrain.png', 
                layout='dot', bg_color='grey22', node_shape='circle', node_color='white', 
                edge_default_color='white', edge_splines='', edge_font_size=10)
```

- Useful reference for parameter customization: [Node, Edge and Graph Attributes in Graphviz](https://graphviz.gitlab.io/_pages/doc/info/attrs.html)
- The function will output both `.dot` file + `.png` file
- Recommended tool for `.dot`: MS Code + [Graphviz Interactive Preview](https://marketplace.visualstudio.com/items?itemName=tintinweb.graphviz-interactive-preview)

## Dependencies

### Graphviz

Ubuntu:

```bash
apt install -y graphviz
```

Windows: 

TODO

### Pygraphviz

Ubuntu:

```bash
apt-get install -y graphviz-dev
pip install pygraphviz
```

Windows: 

TODO

### Fonts

If a language involving non-ascii characters is not corretly shown in the visualization, try to install corresponding fonts.

Example (for Chinese):

Ubuntu:

```bash
apt-get install -y fonts-wqy-microhei
```

## TODO

- Doc: parsing of thebrain10's `thoughts.json` & `links.json`
- Doc: Windows / Mac installation
- Dev: publish package to PYPI
- Dev: correct color mapping (thebrain exported json seems to have bugs about color)
- Layout: label / tag
- Layout: parent / sibling location restriction in visualization
- Layout: community detection
