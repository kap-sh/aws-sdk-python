"""Generated from Smithy shape ``com.amazonaws.databrew#LogSubscription``."""

from typing import Literal, TypeAlias, cast

LogSubscription: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogSubscription) -> str:
    return value


def deserialize_json(data: str) -> LogSubscription:
    return cast(LogSubscription, data)
