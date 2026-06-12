"""Generated from Smithy shape ``com.amazonaws.apigateway#EndpointAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

EndpointAccessMode: TypeAlias = Literal[
    "BASIC",
    "STRICT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "STRICT",
    )
)


def serialize_json(value: EndpointAccessMode) -> str:
    return value


def deserialize_json(data: str) -> EndpointAccessMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointAccessMode value: {data!r}")
    return cast(EndpointAccessMode, data)
