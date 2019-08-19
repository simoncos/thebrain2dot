from pathlib import Path
import sys

p = Path(__file__).absolute()
# make user-profiling in the import system's search list to support running this .py file as script
sys.path.insert(0, str(p.parent.parent))

from thebrain2dot.thebrain2dot import brain_json2dot

if __name__ == '__main__':
    brain_json2dot(thoughts_path='thoughts.json', links_path='links.json')
    # will output both .dot file + .png file
