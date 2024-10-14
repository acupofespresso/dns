# DNS Repository

This repository contains scripts and configurations related to DNS management.

## Features

- DNS resolution for A and CNAME records.
- Latency testing using a ping-like method.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the `dns_resolver.py` script, run the following command:

```bash
echo "your_domain_here" | python3 dns_resolver.py
```

Replace `your_domain_here` with the domain you want to check.

### Example

To check the domain `example.com`, run:

```bash
echo "example.com" | python3 dns_resolver.py
```

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow for contributing to this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
