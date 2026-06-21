"""Generated from Smithy shape ``com.amazonaws.eventbridge#ArchiveState``."""

from typing import Literal, TypeAlias, cast

ArchiveState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "CREATING",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArchiveState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArchiveState:
    return cast(ArchiveState, data)
