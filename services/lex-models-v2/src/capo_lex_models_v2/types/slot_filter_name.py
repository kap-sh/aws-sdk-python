"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotFilterName``."""

from typing import Literal, TypeAlias, cast

SlotFilterName: TypeAlias = Literal["SlotName",]


# --- restJson1 ser/de ---
def serialize_json(value: SlotFilterName) -> str:
    return value


def deserialize_json(data: str) -> SlotFilterName:
    return cast(SlotFilterName, data)
