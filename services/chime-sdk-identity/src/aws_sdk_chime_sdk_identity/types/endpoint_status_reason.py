"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointStatusReason``."""

from typing import Literal, TypeAlias, cast

EndpointStatusReason: TypeAlias = Literal[
    "INVALID_DEVICE_TOKEN",
    "INVALID_PINPOINT_ARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointStatusReason) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatusReason:
    return cast(EndpointStatusReason, data)
