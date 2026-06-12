"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_configuration

WorkflowConfigurationList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.workflow_configuration.WorkflowConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowConfigurationList) -> list:
    import aws_sdk_imagebuilder.types.workflow_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.workflow_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowConfigurationList:
    import aws_sdk_imagebuilder.types.workflow_configuration

    out: WorkflowConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.workflow_configuration.deserialize_json(item)
        )
    return out
