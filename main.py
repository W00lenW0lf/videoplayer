from livereload import Server


def main():
    server = Server()
    server.serve(root='.')


if __name__ == '__main__':
    main()
