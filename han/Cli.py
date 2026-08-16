import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="han",
        description="han-cli - Developer command line toolkit"
    )

    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("name")

    subparsers.add_parser("run")
    subparsers.add_parser("doctor")

    args = parser.parse_args()

    if args.command == "init":
        print(f"Creating project: {args.name}")

    elif args.command == "run":
        print("Starting development server...")

    elif args.command == "doctor":
        print("Checking project...")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
