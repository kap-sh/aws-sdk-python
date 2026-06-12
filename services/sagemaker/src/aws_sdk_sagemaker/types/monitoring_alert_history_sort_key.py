"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertHistorySortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringAlertHistorySortKey: TypeAlias = Literal[
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: MonitoringAlertHistorySortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringAlertHistorySortKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MonitoringAlertHistorySortKey value: {data!r}"
        )
    return cast(MonitoringAlertHistorySortKey, data)
