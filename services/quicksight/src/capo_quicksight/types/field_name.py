"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldName``."""

from typing import Literal, TypeAlias, cast

FieldName: TypeAlias = Literal[
    "assetName",
    "assetDescription",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldName) -> str:
    return value


def deserialize_json(data: str) -> FieldName:
    return cast(FieldName, data)
