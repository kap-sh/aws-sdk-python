"""Generated from Smithy shape ``com.amazonaws.directconnect#InterconnectState``."""

from typing import Literal, TypeAlias, cast

InterconnectState: TypeAlias = Literal[
    "requested",
    "pending",
    "available",
    "down",
    "deleting",
    "deleted",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InterconnectState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InterconnectState:
    return cast(InterconnectState, data)
