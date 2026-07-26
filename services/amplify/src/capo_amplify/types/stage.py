"""Generated from Smithy shape ``com.amazonaws.amplify#Stage``."""

from typing import Literal, TypeAlias, cast

Stage: TypeAlias = Literal[
    "PRODUCTION",
    "BETA",
    "DEVELOPMENT",
    "EXPERIMENTAL",
    "PULL_REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: Stage) -> str:
    return value


def deserialize_json(data: str) -> Stage:
    return cast(Stage, data)
