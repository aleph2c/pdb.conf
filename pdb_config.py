from lxml import etree

def xpp(element):
    try:
        print(etree.tostring(element, pretty_print=True, encoding='unicode'))
    except ImportError:
        print("lxml package is not installed.")

# You can add more functions or configurations here.

