"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LayoutOption``."""

from typing import Literal, TypeAlias, cast

LayoutOption: TypeAlias = Literal["GridView",]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutOption) -> str:
    return value


def deserialize_json(data: str) -> LayoutOption:
    return cast(LayoutOption, data)
