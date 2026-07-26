"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilterOperator``."""

from typing import Literal, TypeAlias, cast

ExportFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> ExportFilterOperator:
    return cast(ExportFilterOperator, data)
