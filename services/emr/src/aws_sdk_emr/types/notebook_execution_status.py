"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

NotebookExecutionStatus: TypeAlias = Literal[
    "START_PENDING",
    "STARTING",
    "RUNNING",
    "FINISHING",
    "FINISHED",
    "FAILING",
    "FAILED",
    "STOP_PENDING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_PENDING",
        "STARTING",
        "RUNNING",
        "FINISHING",
        "FINISHED",
        "FAILING",
        "FAILED",
        "STOP_PENDING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: NotebookExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookExecutionStatus value: {data!r}")
    return cast(NotebookExecutionStatus, data)
