"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#NamespaceDeletionStatus``."""

from typing import Literal, TypeAlias, cast

NamespaceDeletionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceDeletionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceDeletionStatus:
    return cast(NamespaceDeletionStatus, data)
