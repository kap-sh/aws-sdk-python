"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringExecutionSortKey``."""

from typing import Literal, TypeAlias, cast

MonitoringExecutionSortKey: TypeAlias = Literal[
    "CreationTime",
    "ScheduledTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringExecutionSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringExecutionSortKey:
    return cast(MonitoringExecutionSortKey, data)
