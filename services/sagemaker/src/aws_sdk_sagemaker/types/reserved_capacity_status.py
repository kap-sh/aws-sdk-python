"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacityStatus``."""

from typing import Literal, TypeAlias, cast

ReservedCapacityStatus: TypeAlias = Literal[
    "Pending",
    "Active",
    "Scheduled",
    "Expired",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedCapacityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReservedCapacityStatus:
    return cast(ReservedCapacityStatus, data)
