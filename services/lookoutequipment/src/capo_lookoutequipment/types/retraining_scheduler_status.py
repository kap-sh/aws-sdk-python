"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#RetrainingSchedulerStatus``."""

from typing import Literal, TypeAlias, cast

RetrainingSchedulerStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetrainingSchedulerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RetrainingSchedulerStatus:
    return cast(RetrainingSchedulerStatus, data)
