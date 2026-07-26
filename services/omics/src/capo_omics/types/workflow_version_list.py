"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.workflow_version_list_item

WorkflowVersionList: TypeAlias = list[
    "capo_omics.types.workflow_version_list_item.WorkflowVersionListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowVersionList) -> list:
    import capo_omics.types.workflow_version_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.workflow_version_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowVersionList:
    import capo_omics.types.workflow_version_list_item

    out: WorkflowVersionList = []
    for item in data:
        out.append(capo_omics.types.workflow_version_list_item.deserialize_json(item))
    return out
