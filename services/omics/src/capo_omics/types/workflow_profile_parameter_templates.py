"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowProfileParameterTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.workflow_parameter_template
    import capo_omics.types.workflow_profile_name

WorkflowProfileParameterTemplates: TypeAlias = dict[
    "capo_omics.types.workflow_profile_name.WorkflowProfileName",
    "capo_omics.types.workflow_parameter_template.WorkflowParameterTemplate",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkflowProfileParameterTemplates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_omics.types.workflow_parameter_template

        out[key] = capo_omics.types.workflow_parameter_template.serialize_json(value)
    return out


def deserialize_json(data: dict) -> WorkflowProfileParameterTemplates:
    out: WorkflowProfileParameterTemplates = {}
    for key, value in data.items():
        import capo_omics.types.workflow_parameter_template

        out[key] = capo_omics.types.workflow_parameter_template.deserialize_json(value)
    return out
