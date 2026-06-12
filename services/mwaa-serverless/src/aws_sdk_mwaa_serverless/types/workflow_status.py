"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mwaa_serverless.errors import DeserializationError

WorkflowStatus: TypeAlias = Literal[
    "READY",
    "DELETING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "DELETING",
    )
)


def serialize_aws_json_1_0(value: WorkflowStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowStatus value: {data!r}")
    return cast(WorkflowStatus, data)
