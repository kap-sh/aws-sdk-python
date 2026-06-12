"""Generated from Smithy shape ``com.amazonaws.sagemaker#SchedulerConfigComponent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SchedulerConfigComponent: TypeAlias = Literal[
    "PriorityClasses",
    "FairShare",
    "IdleResourceSharing",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PriorityClasses",
        "FairShare",
        "IdleResourceSharing",
    )
)


def serialize_aws_json_1_1(value: SchedulerConfigComponent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchedulerConfigComponent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchedulerConfigComponent value: {data!r}")
    return cast(SchedulerConfigComponent, data)
