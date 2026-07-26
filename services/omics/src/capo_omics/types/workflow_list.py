"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.workflow_list_item

WorkflowList: TypeAlias = list["capo_omics.types.workflow_list_item.WorkflowListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowList) -> list:
    import capo_omics.types.workflow_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.workflow_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowList:
    import capo_omics.types.workflow_list_item

    out: WorkflowList = []
    for item in data:
        out.append(capo_omics.types.workflow_list_item.deserialize_json(item))
    return out
