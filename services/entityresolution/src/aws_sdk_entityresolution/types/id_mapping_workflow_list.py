"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_workflow_summary

IdMappingWorkflowList: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_mapping_workflow_summary.IdMappingWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowList) -> list:
    import aws_sdk_entityresolution.types.id_mapping_workflow_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowList:
    import aws_sdk_entityresolution.types.id_mapping_workflow_summary

    out: IdMappingWorkflowList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_summary.deserialize_json(
                item
            )
        )
    return out
