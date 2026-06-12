"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowParameterDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_parameter_detail

WorkflowParameterDetailList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.workflow_parameter_detail.WorkflowParameterDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameterDetailList) -> list:
    import aws_sdk_imagebuilder.types.workflow_parameter_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.workflow_parameter_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowParameterDetailList:
    import aws_sdk_imagebuilder.types.workflow_parameter_detail

    out: WorkflowParameterDetailList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.workflow_parameter_detail.deserialize_json(item)
        )
    return out
