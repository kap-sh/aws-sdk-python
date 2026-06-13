"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_profile_name

WorkflowProfileList: TypeAlias = list[
    "aws_sdk_omics.types.workflow_profile_name.WorkflowProfileName"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowProfileList) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkflowProfileList:
    return list(data)
