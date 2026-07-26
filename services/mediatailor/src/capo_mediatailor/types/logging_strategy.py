"""Generated from Smithy shape ``com.amazonaws.mediatailor#LoggingStrategy``."""

from typing import Literal, TypeAlias, cast

LoggingStrategy: TypeAlias = Literal[
    "VENDED_LOGS",
    "LEGACY_CLOUDWATCH",
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingStrategy) -> str:
    return value


def deserialize_json(data: str) -> LoggingStrategy:
    return cast(LoggingStrategy, data)
