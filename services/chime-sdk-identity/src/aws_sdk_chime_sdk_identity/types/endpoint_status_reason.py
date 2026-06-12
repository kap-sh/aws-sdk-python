"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

EndpointStatusReason: TypeAlias = Literal[
    "INVALID_DEVICE_TOKEN",
    "INVALID_PINPOINT_ARN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_DEVICE_TOKEN",
        "INVALID_PINPOINT_ARN",
    )
)


def serialize_json(value: EndpointStatusReason) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointStatusReason value: {data!r}")
    return cast(EndpointStatusReason, data)
