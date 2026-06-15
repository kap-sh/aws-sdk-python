"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The lifecycle status of a batch evaluation job.</p>"""
BatchEvaluationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
    "STOPPING",
    "STOPPED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "FAILED",
        "STOPPING",
        "STOPPED",
        "DELETING",
    )
)


def serialize_json(value: BatchEvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> BatchEvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchEvaluationStatus value: {data!r}")
    return cast(BatchEvaluationStatus, data)
