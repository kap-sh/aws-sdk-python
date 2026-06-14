"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ContentHandlingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Specifies how to handle response payload content type conversions. Supported only for WebSocket APIs.</p>"""
ContentHandlingStrategy: TypeAlias = Literal[
    "CONVERT_TO_BINARY",
    "CONVERT_TO_TEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONVERT_TO_BINARY",
        "CONVERT_TO_TEXT",
    )
)


def serialize_json(value: ContentHandlingStrategy) -> str:
    return value


def deserialize_json(data: str) -> ContentHandlingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentHandlingStrategy value: {data!r}")
    return cast(ContentHandlingStrategy, data)
