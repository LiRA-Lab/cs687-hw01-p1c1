# CS 687 · Homework 1 · Project 1, Checkpoint 1

This is a standalone student repository for Homework 1. It introduces
byte-level byte-pair encoding, next-token training windows, embeddings, and the
units used to report language-model loss.

You do not need another CS 687 code repository to complete this homework. A
graphics card is not required.

## What you must complete

The Colab notebook contains ten assessed answer cells:

- four short guided-calculation cells;
- two programming-task cells; and
- four Markdown report-response cells.

The programming tasks are:

| task | tagged notebook cell | function or class |
|---|---|---|
| Task 1 | `answer-task-1` | `BPETokenizer.train` |
| Task 2 | `answer-task-2` | `NextTokenDataset.__init__` |

All six code-answer cells contain `NotImplementedError` placeholders. The
surrounding code is supplied complete. The four report cells contain written
response placeholders. Your completed notebook is the authoritative submission;
you do not need to copy its implementations into `.py` files.

## Grading

Homework 1 is graded out of 100 points:

| assessed work | points |
|---|---:|
| Four guided calculations | 16 |
| Task 1: BPE training | 14 |
| Task 2: sliding-window dataset | 10 |
| Four written responses | 60 |
| **Total** | **100** |

All six code exercises are graded all-or-nothing. Each guided calculation
receives either 4 points or 0 points. Task 1 receives its 14 points only if it
passes every staff-controlled Task 1 test, and Task 2 receives its 10 points
only if it passes every staff-controlled Task 2 test. Partially correct code
does not receive partial credit. The written responses are graded separately.

## Google Colab

Download `notebooks/homework01_colab.ipynb` from this repository and upload it
to Google Colab. Work in that uploaded notebook and save it there; do not
create a new notebook and paste the cells into it, because a new notebook loses
the cell identifiers and metadata that grading depends on. Run the notebook
from top to bottom. Its setup cell clones this repository and installs the
required Python packages. The notebook needs an internet connection once more
after setup, when it downloads GPT-2's tokenizer for the comparison in section
4.

The notebook lets you develop both implementations interactively. A focused
check follows each code-answer cell so that you receive feedback before
continuing. Near the end, a final cell runs all 28 public tests together. Run
these cells inside the notebook: a separate `pytest` process cannot see
definitions that exist only in the notebook kernel.

## Homework workflow

1. Read the Lecture 1 notes.
2. Work through the notebook in order. Complete all four guided-calculation
   cells and the two programming-task cells, and run each immediate check.
3. Restart the runtime and run the complete notebook from top to bottom.
4. Confirm that the final check runs all four calculation checks and reports
   that all 28 programming tests pass.
5. Complete the four questions in the notebook's report section,
   using evidence from your notebook run.

Do not modify the tests to make an implementation pass. The tests describe the
required behavior and grading uses a staff-controlled copy.

## Protect the notebook structure

Automatic grading depends on the released notebook structure. Follow these
rules while working:

- In a code-answer cell, edit only between `YOUR CODE STARTS HERE` and
  `YOUR CODE ENDS HERE`, and keep both marker lines.
- In a written-answer cell, replace only the placeholder below `**Response:**`.
  Do not remove the response marker.
- Do not delete, duplicate, or reorder supplied cells. You may add separate
  scratch cells for your own experiments.
- Do not convert a supplied code cell to Markdown or a supplied Markdown cell
  to code.
- Do not change notebook metadata, cell tags, stable cell IDs, the assignment
  identifier, or the assignment-version number.
- Do not edit supplied instructions, demonstrations, setup code, checks, or
  code outside marked answer regions.

Cell outputs and execution counts do not matter, because grading runs your
notebook again from a fresh kernel.

If you accidentally change the structure, obtain a fresh copy of the released
notebook and copy only your answers into its designated answer regions. A
submission whose structure has changed is set aside for manual inspection and
loses 20 points, because staff have to repair the file by hand before it can
be graded. An answer that cannot be identified reliably receives zero for that
component.

## Deliverables

- the completed Homework 1 notebook

The completed notebook is the single Homework 1 submission. Save the notebook
in Colab, rename it to `homework01_colab_STUDENTNUMBER.ipynb`, replacing
`STUDENTNUMBER` with your student number, for example
`homework01_colab_21802962.ipynb`, and download it with File > Download >
Download .ipynb. Upload that exact file to Moodle. Moodle's account record,
rather than the filename alone, remains the authoritative student identity.
The required filename format is nevertheless mandatory, and a submission
whose file name does not follow it loses 10 points.

You may submit unanswered work; an unanswered cell receives zero for that
component. An unreadable file or a file that is not an `.ipynb` notebook
cannot be graded and receives a grade of zero.

## Repository layout

```text
README.md            this file
requirements.txt     the Python packages the notebook installs
pytest.ini           the test configuration the notebook's checks use
notebook_support.py  supplied setup and public-test helpers
cs687/               supplied implementation modules used by the notebook
tests/               inspectable public tests run by the notebook
data/                the English–Turkish parallel corpus
notebooks/           the Colab entry point and authoritative code submission
```
