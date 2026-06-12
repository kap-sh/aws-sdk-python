"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceSchedulerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

InferenceSchedulerStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: InferenceSchedulerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferenceSchedulerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceSchedulerStatus value: {data!r}")
    return cast(InferenceSchedulerStatus, data)
