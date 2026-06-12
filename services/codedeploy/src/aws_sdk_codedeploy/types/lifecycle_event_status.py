"""Generated from Smithy shape ``com.amazonaws.codedeploy#LifecycleEventStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

LifecycleEventStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "Skipped",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Succeeded",
        "Failed",
        "Skipped",
        "Unknown",
    )
)


def serialize_aws_json_1_1(value: LifecycleEventStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecycleEventStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecycleEventStatus value: {data!r}")
    return cast(LifecycleEventStatus, data)
