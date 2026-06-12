"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowDefinitionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.workflow_definition_summary

WorkflowDefinitionSummaries: TypeAlias = list[
    "aws_sdk_nova_act.types.workflow_definition_summary.WorkflowDefinitionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowDefinitionSummaries) -> list:
    import aws_sdk_nova_act.types.workflow_definition_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_nova_act.types.workflow_definition_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowDefinitionSummaries:
    import aws_sdk_nova_act.types.workflow_definition_summary

    out: WorkflowDefinitionSummaries = []
    for item in data:
        out.append(
            aws_sdk_nova_act.types.workflow_definition_summary.deserialize_json(item)
        )
    return out
