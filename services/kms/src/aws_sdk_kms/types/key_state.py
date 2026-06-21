"""Generated from Smithy shape ``com.amazonaws.kms#KeyState``."""

from typing import Literal, TypeAlias, cast

KeyState: TypeAlias = Literal[
    "Creating",
    "Enabled",
    "Disabled",
    "PendingDeletion",
    "PendingImport",
    "PendingReplicaDeletion",
    "Unavailable",
    "Updating",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyState:
    return cast(KeyState, data)
