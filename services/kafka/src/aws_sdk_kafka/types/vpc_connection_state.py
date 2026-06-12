"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The state of a VPC connection.</p>"""
VpcConnectionState: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "INACTIVE",
    "DEACTIVATING",
    "DELETING",
    "FAILED",
    "REJECTED",
    "REJECTING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "INACTIVE",
        "DEACTIVATING",
        "DELETING",
        "FAILED",
        "REJECTED",
        "REJECTING",
    )
)


def serialize_json(value: VpcConnectionState) -> str:
    return value


def deserialize_json(data: str) -> VpcConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcConnectionState value: {data!r}")
    return cast(VpcConnectionState, data)
