"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_swf.types.workflow_execution_info

WorkflowExecutionInfoList: TypeAlias = list[
    "capo_swf.types.workflow_execution_info.WorkflowExecutionInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionInfoList) -> list:
    import capo_swf.types.workflow_execution_info

    out: list = []
    for item in value:
        out.append(capo_swf.types.workflow_execution_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowExecutionInfoList:
    import capo_swf.types.workflow_execution_info

    out: WorkflowExecutionInfoList = []
    for item in data:
        out.append(
            capo_swf.types.workflow_execution_info.deserialize_aws_json_1_0(item)
        )
    return out
