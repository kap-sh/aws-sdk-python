"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ActionStatus: TypeAlias = Literal[
    "Unknown",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Unknown",
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: ActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionStatus value: {data!r}")
    return cast(ActionStatus, data)
