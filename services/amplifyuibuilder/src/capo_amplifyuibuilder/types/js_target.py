"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#JSTarget``."""

from typing import Literal, TypeAlias, cast

JSTarget: TypeAlias = Literal[
    "es2015",
    "es2020",
]


# --- restJson1 ser/de ---
def serialize_json(value: JSTarget) -> str:
    return value


def deserialize_json(data: str) -> JSTarget:
    return cast(JSTarget, data)
