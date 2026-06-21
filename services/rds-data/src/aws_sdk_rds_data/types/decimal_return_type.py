"""Generated from Smithy shape ``com.amazonaws.rdsdata#DecimalReturnType``."""

from typing import Literal, TypeAlias, cast

DecimalReturnType: TypeAlias = Literal[
    "STRING",
    "DOUBLE_OR_LONG",
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalReturnType) -> str:
    return value


def deserialize_json(data: str) -> DecimalReturnType:
    return cast(DecimalReturnType, data)
