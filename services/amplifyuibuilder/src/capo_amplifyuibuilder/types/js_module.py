"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#JSModule``."""

from typing import Literal, TypeAlias, cast

JSModule: TypeAlias = Literal[
    "es2020",
    "esnext",
]


# --- restJson1 ser/de ---
def serialize_json(value: JSModule) -> str:
    return value


def deserialize_json(data: str) -> JSModule:
    return cast(JSModule, data)
