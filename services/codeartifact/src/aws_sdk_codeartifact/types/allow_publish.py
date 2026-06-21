"""Generated from Smithy shape ``com.amazonaws.codeartifact#AllowPublish``."""

from typing import Literal, TypeAlias, cast

AllowPublish: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowPublish) -> str:
    return value


def deserialize_json(data: str) -> AllowPublish:
    return cast(AllowPublish, data)
