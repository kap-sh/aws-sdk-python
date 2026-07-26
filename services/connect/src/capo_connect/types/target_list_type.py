"""Generated from Smithy shape ``com.amazonaws.connect#TargetListType``."""

from typing import Literal, TypeAlias, cast

TargetListType: TypeAlias = Literal["PROFICIENCIES",]


# --- restJson1 ser/de ---
def serialize_json(value: TargetListType) -> str:
    return value


def deserialize_json(data: str) -> TargetListType:
    return cast(TargetListType, data)
