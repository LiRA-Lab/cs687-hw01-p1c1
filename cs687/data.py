"""
Turning a stream of token ids into training pairs.

Autoregressive training needs pairs of the form (input, target) where the
target is the input shifted forward by one position. One forward pass through
the model then produces a classification loss at every position at once, which
is why the chain-rule factorization the notes derive costs nothing extra at
training time.
"""

import torch
from torch.utils.data import Dataset, DataLoader


class NextTokenDataset(Dataset):
    """Cuts a long stream of token ids into overlapping (input, target) windows.

    For a window starting at position s with context length T:

        input  = ids[s     : s + T]        that is, (y_s,   ..., y_{s+T-1})
        target = ids[s + 1 : s + T + 1]    that is, (y_{s+1}, ..., y_{s+T})

    Args:
        ids: the full stream of token ids, as a plain Python list.
        context_len: how many tokens the model sees at once.
        stride: how far to move the window between consecutive samples.
            A stride smaller than the context length produces overlapping
            windows: more training pairs from the same text, at the cost of
            correlation between them. A stride equal to the context length
            covers the text exactly once with no overlap.
    """

    def __init__(self, ids: list[int], context_len: int, stride: int):
        self.inputs: list[torch.Tensor] = []
        self.targets: list[torch.Tensor] = []

        # This is Task 2 of the homework. The notebook describes the loop, you
        # write it in the notebook's answer cell, and the check after that cell
        # attaches your class to this module in place of this stub.
        raise NotImplementedError(
            "Task 2 is written in the homework notebook, which attaches the class to this module."
        )

    def __len__(self) -> int:
        return len(self.inputs)

    def __getitem__(self, i: int) -> tuple[torch.Tensor, torch.Tensor]:
        return self.inputs[i], self.targets[i]


def make_loader(
    ids: list[int],
    context_len: int = 256,
    stride: int = 128,
    batch_size: int = 8,
    shuffle: bool = True,
) -> DataLoader:
    """Wrap NextTokenDataset in a DataLoader. Supplied complete."""
    dataset = NextTokenDataset(ids, context_len, stride)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, drop_last=True)
