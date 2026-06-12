"""Generated from Smithy shape ``com.amazonaws.apigateway#VpcLinkStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

VpcLinkStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: VpcLinkStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcLinkStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcLinkStatus value: {data!r}")
    return cast(VpcLinkStatus, data)
