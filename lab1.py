from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD  # Get the global communicator
    rank = comm.Get_rank()  # Get process ID (rank)
    size = comm.Get_size()  # Get total number of processes

    print(f"Process {rank} out of {size}")

if __name__ == "__main__":
    main()
