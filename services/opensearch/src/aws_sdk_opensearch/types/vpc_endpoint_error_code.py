"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

VpcEndpointErrorCode: TypeAlias = Literal[
    "ENDPOINT_NOT_FOUND",
    "SERVER_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENDPOINT_NOT_FOUND",
        "SERVER_ERROR",
    )
)


def serialize_json(value: VpcEndpointErrorCode) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcEndpointErrorCode value: {data!r}")
    return cast(VpcEndpointErrorCode, data)
