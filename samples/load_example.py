from pathlib import Path
import numpy as np

root = Path(__file__).resolve().parent
participant = next(iter(sorted((root / "subjects").iterdir())))
data = {p.stem: np.load(p, mmap_mode="r", allow_pickle=False)
        for p in sorted(participant.glob("*.npy"))}
for name, values in data.items():
    print(name, values.shape, values.dtype)
