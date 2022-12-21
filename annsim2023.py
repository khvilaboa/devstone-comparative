import subprocess


if __name__ == '__main__':
    a = "adevs,xdevs-c,xdevs-cpp,xdevs-rs,xdevs-java-sequential"
    models = [['LI', 'HI', 'HO'], ['HOmod']]
    sizes = [list(range(20, 401, 20)), list(range(10, 101, 10))]
    p = []
    for i, models in enumerate(models):
        p.extend([f'{m}-{w}-{d}-0-0' for m in models for w in sizes[i] for d in sizes[i]])
    p = ','.join(p)
    n = 30
    o = "annsim2023.csv"

    cmd = f"python3 devstone_comparative.py -a {a} -p {p} -n {n} -o {o}"
    subprocess.run(cmd.split())
