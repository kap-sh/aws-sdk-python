"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertHistorySortKey``."""

from typing import Literal, TypeAlias, cast

MonitoringAlertHistorySortKey: TypeAlias = Literal[
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertHistorySortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringAlertHistorySortKey:
    return cast(MonitoringAlertHistorySortKey, data)
