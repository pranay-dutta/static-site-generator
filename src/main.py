from textnode import TextNode, TextType


def main():
    text = "This is some anchor text"
    text_type = TextType.LINK
    url = "https://www.boot.dev"

    textnode = TextNode(text=text, text_type=text_type, url=url)
    print(textnode)


if __name__ == "__main__":
    main()
