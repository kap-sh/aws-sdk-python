"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#LoggingLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The logging level.</p>"""
LoggingLevel: TypeAlias = Literal[
    "ERROR",
    "INFO",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "INFO",
        "OFF",
    )
)


def serialize_json(value: LoggingLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggingLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggingLevel value: {data!r}")
    return cast(LoggingLevel, data)
