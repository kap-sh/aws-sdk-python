"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

BGPPeerState: TypeAlias = Literal[
    "verifying",
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "verifying",
        "pending",
        "available",
        "deleting",
        "deleted",
    )
)


def serialize_aws_json_1_1(value: BGPPeerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BGPPeerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BGPPeerState value: {data!r}")
    return cast(BGPPeerState, data)
