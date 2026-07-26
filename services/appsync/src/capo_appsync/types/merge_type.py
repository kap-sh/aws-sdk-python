"""Generated from Smithy shape ``com.amazonaws.appsync#MergeType``."""

from typing import Literal, TypeAlias, cast

MergeType: TypeAlias = Literal[
    "MANUAL_MERGE",
    "AUTO_MERGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MergeType) -> str:
    return value


def deserialize_json(data: str) -> MergeType:
    return cast(MergeType, data)
