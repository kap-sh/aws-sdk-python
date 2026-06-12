"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringAlertStatus: TypeAlias = Literal[
    "InAlert",
    "OK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InAlert",
        "OK",
    )
)


def serialize_aws_json_1_1(value: MonitoringAlertStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringAlertStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitoringAlertStatus value: {data!r}")
    return cast(MonitoringAlertStatus, data)
