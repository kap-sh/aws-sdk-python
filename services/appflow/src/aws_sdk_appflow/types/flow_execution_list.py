"""Generated from Smithy shape ``com.amazonaws.appflow#FlowExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.execution_record

FlowExecutionList: TypeAlias = list[
    "aws_sdk_appflow.types.execution_record.ExecutionRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionList) -> list:
    import aws_sdk_appflow.types.execution_record

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.execution_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowExecutionList:
    import aws_sdk_appflow.types.execution_record

    out: FlowExecutionList = []
    for item in data:
        out.append(aws_sdk_appflow.types.execution_record.deserialize_json(item))
    return out
