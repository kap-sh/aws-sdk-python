"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeerState``."""

from typing import Literal, TypeAlias, cast

BGPPeerState: TypeAlias = Literal[
    "verifying",
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BGPPeerState:
    return cast(BGPPeerState, data)
