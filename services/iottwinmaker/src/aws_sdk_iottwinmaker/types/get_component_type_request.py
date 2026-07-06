"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetComponentTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.id


class GetComponentTypeRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the component type.</p>"""
    component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentTypeRequest:
    out: GetComponentTypeRequest = {}  # type: ignore[typeddict-item]
    return out
