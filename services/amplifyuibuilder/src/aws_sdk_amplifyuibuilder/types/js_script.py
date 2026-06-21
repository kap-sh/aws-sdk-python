"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#JSScript``."""

from typing import Literal, TypeAlias, cast

JSScript: TypeAlias = Literal[
    "jsx",
    "tsx",
    "js",
]


# --- restJson1 ser/de ---
def serialize_json(value: JSScript) -> str:
    return value


def deserialize_json(data: str) -> JSScript:
    return cast(JSScript, data)
