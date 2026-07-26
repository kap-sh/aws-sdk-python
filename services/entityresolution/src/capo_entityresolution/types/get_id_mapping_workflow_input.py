"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetIdMappingWorkflowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name


class GetIdMappingWorkflowInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingWorkflowInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdMappingWorkflowInput:
    out: GetIdMappingWorkflowInput = {}  # type: ignore[typeddict-item]
    return out
