"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

AttachmentStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "ERROR",
    "SCALING",
    "READY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "FAILED",
        "ERROR",
        "SCALING",
        "READY",
    )
)


def serialize_aws_json_1_0(value: AttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AttachmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentStatus value: {data!r}")
    return cast(AttachmentStatus, data)
