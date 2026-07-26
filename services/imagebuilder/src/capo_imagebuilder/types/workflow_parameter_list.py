"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_parameter

WorkflowParameterList: TypeAlias = list[
    "capo_imagebuilder.types.workflow_parameter.WorkflowParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameterList) -> list:
    import capo_imagebuilder.types.workflow_parameter

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.workflow_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowParameterList:
    import capo_imagebuilder.types.workflow_parameter

    out: WorkflowParameterList = []
    for item in data:
        out.append(capo_imagebuilder.types.workflow_parameter.deserialize_json(item))
    return out
