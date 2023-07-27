import pandas as pd
import sys
import os

def split_csv(input_file, chunk_size):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Determine the number of chunks needed
    total_rows = df.shape[0]
    num_chunks = (total_rows - 1) // chunk_size + 1
    
    # Get the base filename (without extension) from the input file
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Split the DataFrame into chunks and save them to separate CSV files
    for i, chunk_start in enumerate(range(0, total_rows, chunk_size)):
        chunk_end = min(chunk_start + chunk_size, total_rows)
        chunk = df.iloc[chunk_start:chunk_end]
        output_file = f"{base_filename}_part{i+1}.csv"
        chunk.to_csv(output_file, index=False)
        print(f"Chunk {i+1} saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_file_path> <chunk_size>")
    else:
        input_file_path = sys.argv[1]
        chunk_size = int(sys.argv[2])
        split_csv(input_file_path, chunk_size)
