"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringScheduleSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringScheduleSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: MonitoringScheduleSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringScheduleSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitoringScheduleSortKey value: {data!r}")
    return cast(MonitoringScheduleSortKey, data)
