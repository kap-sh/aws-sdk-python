"""Generated from Smithy shape ``com.amazonaws.transfer#WorkflowStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

WorkflowStepType: TypeAlias = Literal[
    "COPY",
    "CUSTOM",
    "TAG",
    "DELETE",
    "DECRYPT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COPY",
        "CUSTOM",
        "TAG",
        "DELETE",
        "DECRYPT",
    )
)


def serialize_aws_json_1_1(value: WorkflowStepType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkflowStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowStepType value: {data!r}")
    return cast(WorkflowStepType, data)
