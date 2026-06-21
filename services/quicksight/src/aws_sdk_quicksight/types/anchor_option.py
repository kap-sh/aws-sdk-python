"""Generated from Smithy shape ``com.amazonaws.quicksight#AnchorOption``."""

from typing import Literal, TypeAlias, cast

AnchorOption: TypeAlias = Literal["NOW",]


# --- restJson1 ser/de ---
def serialize_json(value: AnchorOption) -> str:
    return value


def deserialize_json(data: str) -> AnchorOption:
    return cast(AnchorOption, data)
