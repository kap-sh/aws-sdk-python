"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertStatus``."""

from typing import Literal, TypeAlias, cast

MonitoringAlertStatus: TypeAlias = Literal[
    "InAlert",
    "OK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringAlertStatus:
    return cast(MonitoringAlertStatus, data)
