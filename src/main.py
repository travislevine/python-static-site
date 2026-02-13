from textnode import TextNode, TextType

def main():
    my_textnode = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(my_textnode)
main()