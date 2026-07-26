"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_version

WorkflowVersionList: TypeAlias = list[
    "capo_imagebuilder.types.workflow_version.WorkflowVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowVersionList) -> list:
    import capo_imagebuilder.types.workflow_version

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.workflow_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowVersionList:
    import capo_imagebuilder.types.workflow_version

    out: WorkflowVersionList = []
    for item in data:
        out.append(capo_imagebuilder.types.workflow_version.deserialize_json(item))
    return out
