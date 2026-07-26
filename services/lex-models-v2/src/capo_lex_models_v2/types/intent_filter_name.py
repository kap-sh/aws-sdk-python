"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilterName``."""

from typing import Literal, TypeAlias, cast

IntentFilterName: TypeAlias = Literal["IntentName",]


# --- restJson1 ser/de ---
def serialize_json(value: IntentFilterName) -> str:
    return value


def deserialize_json(data: str) -> IntentFilterName:
    return cast(IntentFilterName, data)
