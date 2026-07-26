"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_workflow_summary

IdMappingWorkflowList: TypeAlias = list[
    "capo_entityresolution.types.id_mapping_workflow_summary.IdMappingWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowList) -> list:
    import capo_entityresolution.types.id_mapping_workflow_summary

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_mapping_workflow_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowList:
    import capo_entityresolution.types.id_mapping_workflow_summary

    out: IdMappingWorkflowList = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_mapping_workflow_summary.deserialize_json(
                item
            )
        )
    return out
