"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#XAxisType``."""

from typing import Literal, TypeAlias, cast

XAxisType: TypeAlias = Literal[
    "IterationNumber",
    "Timestamp",
]


# --- restJson1 ser/de ---
def serialize_json(value: XAxisType) -> str:
    return value


def deserialize_json(data: str) -> XAxisType:
    return cast(XAxisType, data)
