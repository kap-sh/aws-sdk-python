"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_parameter_value

WorkflowParameterValueList: TypeAlias = list[
    "capo_imagebuilder.types.workflow_parameter_value.WorkflowParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkflowParameterValueList:
    return list(data)
