"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: BatchEvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> BatchEvaluationStatus:
    return cast(BatchEvaluationStatus, data)
