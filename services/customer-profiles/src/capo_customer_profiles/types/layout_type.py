"""Generated from Smithy shape ``com.amazonaws.customerprofiles#LayoutType``."""

from typing import Literal, TypeAlias, cast

LayoutType: TypeAlias = Literal["PROFILE_EXPLORER",]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutType) -> str:
    return value


def deserialize_json(data: str) -> LayoutType:
    return cast(LayoutType, data)
