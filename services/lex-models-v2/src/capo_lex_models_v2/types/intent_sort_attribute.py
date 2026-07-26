"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentSortAttribute``."""

from typing import Literal, TypeAlias, cast

IntentSortAttribute: TypeAlias = Literal[
    "IntentName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> IntentSortAttribute:
    return cast(IntentSortAttribute, data)
