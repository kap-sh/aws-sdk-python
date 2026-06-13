"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowProfileParameterTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_parameter_template
    import aws_sdk_omics.types.workflow_profile_name

WorkflowProfileParameterTemplates: TypeAlias = dict[
    "aws_sdk_omics.types.workflow_profile_name.WorkflowProfileName",
    "aws_sdk_omics.types.workflow_parameter_template.WorkflowParameterTemplate",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkflowProfileParameterTemplates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_omics.types.workflow_parameter_template

        out[key] = aws_sdk_omics.types.workflow_parameter_template.serialize_json(value)
    return out


def deserialize_json(data: dict) -> WorkflowProfileParameterTemplates:
    out: WorkflowProfileParameterTemplates = {}
    for key, value in data.items():
        import aws_sdk_omics.types.workflow_parameter_template

        out[key] = aws_sdk_omics.types.workflow_parameter_template.deserialize_json(
            value
        )
    return out
