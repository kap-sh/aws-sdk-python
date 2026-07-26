"""Generated from Smithy shape ``com.amazonaws.quicksight#AnchorType``."""

from typing import Literal, TypeAlias, cast

AnchorType: TypeAlias = Literal["TODAY",]


# --- restJson1 ser/de ---
def serialize_json(value: AnchorType) -> str:
    return value


def deserialize_json(data: str) -> AnchorType:
    return cast(AnchorType, data)
