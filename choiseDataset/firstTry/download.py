import kagglehub

# Enter the API token in the terminal when prompted.
kagglehub.login()

# Download latest version
path = kagglehub.competition_download('severstal-steel-defect-detection')

print("Path to competition files:", path)
