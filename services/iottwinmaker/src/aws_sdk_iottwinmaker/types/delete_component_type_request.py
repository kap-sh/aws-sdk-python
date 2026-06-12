"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteComponentTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.id


class DeleteComponentTypeRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the component type.</p>"""
    component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComponentTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteComponentTypeRequest:
    out: DeleteComponentTypeRequest = {}  # type: ignore[typeddict-item]
    return out
