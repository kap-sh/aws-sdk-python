"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointErrorCode``."""

from typing import Literal, TypeAlias, cast

VpcEndpointErrorCode: TypeAlias = Literal[
    "ENDPOINT_NOT_FOUND",
    "SERVER_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointErrorCode) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointErrorCode:
    return cast(VpcEndpointErrorCode, data)
