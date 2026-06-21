"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowExecutionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of instance.</p>"""
JobFlowExecutionState: TypeAlias = Literal[
    "STARTING",
    "BOOTSTRAPPING",
    "RUNNING",
    "WAITING",
    "SHUTTING_DOWN",
    "TERMINATED",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobFlowExecutionState:
    return cast(JobFlowExecutionState, data)
