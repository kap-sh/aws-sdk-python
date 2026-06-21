"""Generated from Smithy shape ``com.amazonaws.appsync#HandlerBehavior``."""

from typing import Literal, TypeAlias, cast

HandlerBehavior: TypeAlias = Literal[
    "CODE",
    "DIRECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: HandlerBehavior) -> str:
    return value


def deserialize_json(data: str) -> HandlerBehavior:
    return cast(HandlerBehavior, data)
