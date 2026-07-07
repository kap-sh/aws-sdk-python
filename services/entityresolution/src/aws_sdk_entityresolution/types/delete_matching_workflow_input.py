"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteMatchingWorkflowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class DeleteMatchingWorkflowInput(TypedDict, closed=True):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMatchingWorkflowInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMatchingWorkflowInput:
    out: DeleteMatchingWorkflowInput = {}  # type: ignore[typeddict-item]
    return out
