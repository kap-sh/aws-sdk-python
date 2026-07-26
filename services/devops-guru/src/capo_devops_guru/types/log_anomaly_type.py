"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogAnomalyType``."""

from typing import Literal, TypeAlias, cast

LogAnomalyType: TypeAlias = Literal[
    "KEYWORD",
    "KEYWORD_TOKEN",
    "FORMAT",
    "HTTP_CODE",
    "BLOCK_FORMAT",
    "NUMERICAL_POINT",
    "NUMERICAL_NAN",
    "NEW_FIELD_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogAnomalyType) -> str:
    return value


def deserialize_json(data: str) -> LogAnomalyType:
    return cast(LogAnomalyType, data)
