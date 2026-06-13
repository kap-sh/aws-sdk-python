"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteIdMappingWorkflowInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class DeleteIdMappingWorkflowInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdMappingWorkflowInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdMappingWorkflowInput:
    out: DeleteIdMappingWorkflowInput = {}  # type: ignore[typeddict-item]
    return out
