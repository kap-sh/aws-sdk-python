"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowParameterTemplate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.workflow_parameter
    import capo_omics.types.workflow_parameter_name

WorkflowParameterTemplate: TypeAlias = dict[
    "capo_omics.types.workflow_parameter_name.WorkflowParameterName",
    "capo_omics.types.workflow_parameter.WorkflowParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkflowParameterTemplate) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_omics.types.workflow_parameter

        out[key] = capo_omics.types.workflow_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> WorkflowParameterTemplate:
    out: WorkflowParameterTemplate = {}
    for key, value in data.items():
        import capo_omics.types.workflow_parameter

        out[key] = capo_omics.types.workflow_parameter.deserialize_json(value)
    return out
