"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringExecutionSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringExecutionSortKey: TypeAlias = Literal[
    "CreationTime",
    "ScheduledTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "ScheduledTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: MonitoringExecutionSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringExecutionSortKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MonitoringExecutionSortKey value: {data!r}"
        )
    return cast(MonitoringExecutionSortKey, data)
