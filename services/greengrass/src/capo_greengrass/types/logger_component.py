"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerComponent``."""

from typing import Literal, TypeAlias, cast

LoggerComponent: TypeAlias = Literal[
    "GreengrassSystem",
    "Lambda",
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggerComponent) -> str:
    return value


def deserialize_json(data: str) -> LoggerComponent:
    return cast(LoggerComponent, data)
