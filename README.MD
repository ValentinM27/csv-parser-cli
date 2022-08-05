# CSV PARSER CLI
Simple command line tool to parse and convert CSV files into JSON files.

## Required install
You should have python3 installed on your machine,
if you want to use the ```make``` command you should be on either macOS or Linux.

## How to use ?
Go to the project directory and use the following command :

### Make command:
```
make csv-parse path=< PATH TO YOUR CSV > to=< PATH FOR YOUR JSON >
```

### Python command:
```
python3 main.py < PATH TO YOUR CSV > < PATH FOR YOUR JSON >
```

Take notice that the JSON file will be create if it doesn't already exist.

## References
The test file come from https://people.sc.fsu.edu/