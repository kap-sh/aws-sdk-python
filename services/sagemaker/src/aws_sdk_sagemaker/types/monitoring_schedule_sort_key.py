"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringScheduleSortKey``."""

from typing import Literal, TypeAlias, cast

MonitoringScheduleSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringScheduleSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringScheduleSortKey:
    return cast(MonitoringScheduleSortKey, data)
