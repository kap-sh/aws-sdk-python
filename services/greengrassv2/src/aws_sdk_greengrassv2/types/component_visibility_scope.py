"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentVisibilityScope``."""

from typing import Literal, TypeAlias, cast

ComponentVisibilityScope: TypeAlias = Literal[
    "PRIVATE",
    "PUBLIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVisibilityScope) -> str:
    return value


def deserialize_json(data: str) -> ComponentVisibilityScope:
    return cast(ComponentVisibilityScope, data)
