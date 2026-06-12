"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringJobDefinitionSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringJobDefinitionSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: MonitoringJobDefinitionSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringJobDefinitionSortKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MonitoringJobDefinitionSortKey value: {data!r}"
        )
    return cast(MonitoringJobDefinitionSortKey, data)
