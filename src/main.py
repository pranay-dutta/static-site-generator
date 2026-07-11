from textnode import TextNode, TextType
from copy_static import copy_files_recursive
import os
import shutil

static_path = "./static"
public_path = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    print("Copying static files to public directory.")
    copy_files_recursive(static_path, public_path)


if __name__ == "__main__":
    main()
