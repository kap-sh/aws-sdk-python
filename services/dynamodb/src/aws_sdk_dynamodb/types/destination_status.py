"""Generated from Smithy shape ``com.amazonaws.dynamodb#DestinationStatus``."""

from typing import Literal, TypeAlias, cast

DestinationStatus: TypeAlias = Literal[
    "ENABLING",
    "ACTIVE",
    "DISABLING",
    "DISABLED",
    "ENABLE_FAILED",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DestinationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DestinationStatus:
    return cast(DestinationStatus, data)
