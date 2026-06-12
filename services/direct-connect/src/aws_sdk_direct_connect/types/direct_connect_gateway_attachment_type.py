"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAttachmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

DirectConnectGatewayAttachmentType: TypeAlias = Literal[
    "TransitVirtualInterface",
    "PrivateVirtualInterface",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TransitVirtualInterface",
        "PrivateVirtualInterface",
    )
)


def serialize_aws_json_1_1(value: DirectConnectGatewayAttachmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAttachmentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectConnectGatewayAttachmentType value: {data!r}"
        )
    return cast(DirectConnectGatewayAttachmentType, data)
