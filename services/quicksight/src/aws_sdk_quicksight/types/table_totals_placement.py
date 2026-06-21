"""Generated from Smithy shape ``com.amazonaws.quicksight#TableTotalsPlacement``."""

from typing import Literal, TypeAlias, cast

TableTotalsPlacement: TypeAlias = Literal[
    "START",
    "END",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableTotalsPlacement) -> str:
    return value


def deserialize_json(data: str) -> TableTotalsPlacement:
    return cast(TableTotalsPlacement, data)
