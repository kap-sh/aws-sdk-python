"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

NotebookInstanceStatus: TypeAlias = Literal[
    "Pending",
    "InService",
    "Stopping",
    "Stopped",
    "Failed",
    "Deleting",
    "Updating",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InService",
        "Stopping",
        "Stopped",
        "Failed",
        "Deleting",
        "Updating",
    )
)


def serialize_aws_json_1_1(value: NotebookInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookInstanceStatus value: {data!r}")
    return cast(NotebookInstanceStatus, data)
