"""Generated from Smithy shape ``com.amazonaws.quicksight#PaperSize``."""

from typing import Literal, TypeAlias, cast

PaperSize: TypeAlias = Literal[
    "US_LETTER",
    "US_LEGAL",
    "US_TABLOID_LEDGER",
    "A0",
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "JIS_B4",
    "JIS_B5",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaperSize) -> str:
    return value


def deserialize_json(data: str) -> PaperSize:
    return cast(PaperSize, data)
