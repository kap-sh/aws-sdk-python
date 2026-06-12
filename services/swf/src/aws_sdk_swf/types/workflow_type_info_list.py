"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_swf.types.workflow_type_info

WorkflowTypeInfoList: TypeAlias = list[
    "aws_sdk_swf.types.workflow_type_info.WorkflowTypeInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeInfoList) -> list:
    import aws_sdk_swf.types.workflow_type_info

    out: list = []
    for item in value:
        out.append(aws_sdk_swf.types.workflow_type_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowTypeInfoList:
    import aws_sdk_swf.types.workflow_type_info

    out: WorkflowTypeInfoList = []
    for item in data:
        out.append(aws_sdk_swf.types.workflow_type_info.deserialize_aws_json_1_0(item))
    return out
