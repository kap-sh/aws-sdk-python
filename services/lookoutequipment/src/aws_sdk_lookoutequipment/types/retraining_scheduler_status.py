"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#RetrainingSchedulerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

RetrainingSchedulerStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_0(value: RetrainingSchedulerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RetrainingSchedulerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrainingSchedulerStatus value: {data!r}")
    return cast(RetrainingSchedulerStatus, data)
