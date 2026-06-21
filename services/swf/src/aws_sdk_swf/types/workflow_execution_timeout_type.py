"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTimeoutType``."""

from typing import Literal, TypeAlias, cast

WorkflowExecutionTimeoutType: TypeAlias = Literal["START_TO_CLOSE",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowExecutionTimeoutType:
    return cast(WorkflowExecutionTimeoutType, data)
