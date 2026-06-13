"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchingWorkflowInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class GetMatchingWorkflowInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchingWorkflowInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMatchingWorkflowInput:
    out: GetMatchingWorkflowInput = {}  # type: ignore[typeddict-item]
    return out
