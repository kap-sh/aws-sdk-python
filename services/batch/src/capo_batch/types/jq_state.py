"""Generated from Smithy shape ``com.amazonaws.batch#JQState``."""

from typing import Literal, TypeAlias, cast

JQState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JQState) -> str:
    return value


def deserialize_json(data: str) -> JQState:
    return cast(JQState, data)
