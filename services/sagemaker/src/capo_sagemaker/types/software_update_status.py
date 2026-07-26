"""Generated from Smithy shape ``com.amazonaws.sagemaker#SoftwareUpdateStatus``."""

from typing import Literal, TypeAlias, cast

SoftwareUpdateStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "RollbackInProgress",
    "RollbackComplete",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SoftwareUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SoftwareUpdateStatus:
    return cast(SoftwareUpdateStatus, data)
