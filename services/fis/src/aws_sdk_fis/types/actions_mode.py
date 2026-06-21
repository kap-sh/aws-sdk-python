"""Generated from Smithy shape ``com.amazonaws.fis#ActionsMode``."""

from typing import Literal, TypeAlias, cast

ActionsMode: TypeAlias = Literal[
    "skip-all",
    "run-all",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionsMode) -> str:
    return value


def deserialize_json(data: str) -> ActionsMode:
    return cast(ActionsMode, data)
