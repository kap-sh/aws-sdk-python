"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionState``."""

from typing import Literal, TypeAlias, cast

QueryExecutionState: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryExecutionState:
    return cast(QueryExecutionState, data)
