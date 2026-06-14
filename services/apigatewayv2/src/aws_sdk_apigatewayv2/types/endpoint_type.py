"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Represents an endpoint type.</p>"""
EndpointType: TypeAlias = Literal[
    "REGIONAL",
    "EDGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGIONAL",
        "EDGE",
    )
)


def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
