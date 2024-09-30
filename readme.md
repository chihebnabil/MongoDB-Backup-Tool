# MongoDB Export and Import Scripts

This repository contains two Python scripts for exporting data from a MongoDB database and importing it back. These scripts are useful for backing up your MongoDB data or migrating it between different environments.

## Requirements

- Python 3.6+
- pymongo library
- bson library

Install the required libraries using pip:

```
pip install pymongo bson
```

## Export Script (export_script.py)

This script exports all collections from a specified MongoDB database to a JSON file.

### Usage

```
python export.py <mongodb_url> <output_file>
```

- `<mongodb_url>`: The MongoDB connection string URL.
- `<output_file>`: The name of the JSON file where the data will be exported.

### Example

```
python export.py "mongodb://username:password@localhost:27017/mydb" output.json
```

## Import Script (import_script.py)

This script imports data from a JSON file (created by the export script) into a MongoDB database.

### Usage

```
python import.py <mongodb_url> <input_file>
```

- `<mongodb_url>`: The MongoDB connection string URL.
- `<input_file>`: The name of the JSON file containing the data to be imported.

### Example

```
python import.py "mongodb://username:password@localhost:27017/mydb" input.json
```

## Important Notes

1. The import script will overwrite existing data in the collections. Make sure you have a backup before importing.

2. These scripts handle BSON types (like ObjectId) correctly during export and import.

3. For large databases, the export and import processes may take some time. Be patient and ensure you have a stable connection.

4. Always test these scripts in a non-production environment before using them with live data.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the correct permissions to access the MongoDB database.
2. Check that your MongoDB URL is correct and includes the database name.
3. Verify that the JSON file structure matches what's expected by the import script.

If problems persist, check the error messages for more details on what might be going wrong.

## Security Warning

These scripts contain sensitive information like database URLs. Never commit these scripts with real credentials to a public repository. Use environment variables or configuration files to manage sensitive information securely.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open-source and available under the MIT License.
