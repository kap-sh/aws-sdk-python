"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

VirtualInterfaceState: TypeAlias = Literal[
    "confirming",
    "verifying",
    "pending",
    "available",
    "down",
    "testing",
    "deleting",
    "deleted",
    "rejected",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "confirming",
        "verifying",
        "pending",
        "available",
        "down",
        "testing",
        "deleting",
        "deleted",
        "rejected",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: VirtualInterfaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VirtualInterfaceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VirtualInterfaceState value: {data!r}")
    return cast(VirtualInterfaceState, data)
