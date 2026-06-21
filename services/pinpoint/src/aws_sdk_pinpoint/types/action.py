"""Generated from Smithy shape ``com.amazonaws.pinpoint#Action``."""

from typing import Literal, TypeAlias, cast

Action: TypeAlias = Literal[
    "OPEN_APP",
    "DEEP_LINK",
    "URL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    return cast(Action, data)
