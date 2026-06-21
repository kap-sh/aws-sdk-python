"""Generated from Smithy shape ``com.amazonaws.quicksight#TableTotalsScrollStatus``."""

from typing import Literal, TypeAlias, cast

TableTotalsScrollStatus: TypeAlias = Literal[
    "PINNED",
    "SCROLLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableTotalsScrollStatus) -> str:
    return value


def deserialize_json(data: str) -> TableTotalsScrollStatus:
    return cast(TableTotalsScrollStatus, data)
