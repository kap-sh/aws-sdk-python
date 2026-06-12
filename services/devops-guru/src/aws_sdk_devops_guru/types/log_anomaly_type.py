"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogAnomalyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "KEYWORD",
        "KEYWORD_TOKEN",
        "FORMAT",
        "HTTP_CODE",
        "BLOCK_FORMAT",
        "NUMERICAL_POINT",
        "NUMERICAL_NAN",
        "NEW_FIELD_NAME",
    )
)


def serialize_json(value: LogAnomalyType) -> str:
    return value


def deserialize_json(data: str) -> LogAnomalyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogAnomalyType value: {data!r}")
    return cast(LogAnomalyType, data)
