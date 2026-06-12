"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

InferenceExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: InferenceExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferenceExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceExecutionStatus value: {data!r}")
    return cast(InferenceExecutionStatus, data)
