"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAttachmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

DirectConnectGatewayAttachmentState: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "attaching",
        "attached",
        "detaching",
        "detached",
    )
)


def serialize_aws_json_1_1(value: DirectConnectGatewayAttachmentState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectConnectGatewayAttachmentState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectConnectGatewayAttachmentState value: {data!r}"
        )
    return cast(DirectConnectGatewayAttachmentState, data)
