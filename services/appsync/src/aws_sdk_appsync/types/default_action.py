"""Generated from Smithy shape ``com.amazonaws.appsync#DefaultAction``."""

from typing import Literal, TypeAlias, cast

DefaultAction: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultAction) -> str:
    return value


def deserialize_json(data: str) -> DefaultAction:
    return cast(DefaultAction, data)
