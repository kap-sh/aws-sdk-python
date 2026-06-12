"""Generated from Smithy shape ``com.amazonaws.codeartifact#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

EndpointType: TypeAlias = Literal[
    "dualstack",
    "ipv4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "dualstack",
        "ipv4",
    )
)


def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
