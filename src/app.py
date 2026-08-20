"""demoapp-backend — stand-in service for the n8n CI/CD demo."""

VERSION = "1.0.0"
LOG_LEVEL = "DEBUG"


def main() -> None:
    print(f"demoapp-backend {VERSION} starting (log level {LOG_LEVEL})")


if __name__ == "__main__":
    main()
