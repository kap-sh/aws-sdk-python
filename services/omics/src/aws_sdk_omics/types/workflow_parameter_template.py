"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowParameterTemplate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_parameter
    import aws_sdk_omics.types.workflow_parameter_name

WorkflowParameterTemplate: TypeAlias = dict[
    "aws_sdk_omics.types.workflow_parameter_name.WorkflowParameterName",
    "aws_sdk_omics.types.workflow_parameter.WorkflowParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkflowParameterTemplate) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_omics.types.workflow_parameter

        out[key] = aws_sdk_omics.types.workflow_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> WorkflowParameterTemplate:
    out: WorkflowParameterTemplate = {}
    for key, value in data.items():
        import aws_sdk_omics.types.workflow_parameter

        out[key] = aws_sdk_omics.types.workflow_parameter.deserialize_json(value)
    return out
