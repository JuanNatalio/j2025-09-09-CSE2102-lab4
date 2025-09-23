# j2025-09-09-CSE2102-lab4

## Lab 4: Basic HTTP with Python Flask

This project demonstrates a simple Flask server with an endpoint to factor integers. The `/factors` endpoint receives an integer and returns its factors as a list. If the number is prime, it returns a list with just that number. If the number is 1, it returns `[1]`.

### How to Run the Server

1. Install Flask if needed:
	```bash
	pip install flask
	```
2. Start the server:
	```bash
	python3 my_server.py
	```
3. Use `curl` or Postman to test the endpoint:
	```bash
	curl -d "inINT=12" -X POST https://super-duper-space-barnacle-r4wgr747xwpxcpqjp-5000.app.github.dev/factors
	# Response: {"factors": [2, 2, 3]}
	```

### How to Run the Unit Tests

```bash
python3 test_factors.py
```

### Brief Description

- Added a `/factors` endpoint to the Flask server that receives an integer and returns its factors using trial division.
- Included unit tests for the factoring logic.
- See `my_server.py` for the server code and `test_factors.py` for tests.