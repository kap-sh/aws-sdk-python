"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.component_type_id


class CompositeComponentTypeResponse(TypedDict):
    component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>This is the <code>componentTypeId</code> that this <code>compositeComponentType</code> refers to.</p>"""
    is_inherited: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>This boolean indicates whether this <code>compositeComponentType</code> is inherited from its parent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeComponentTypeResponse) -> dict:
    out: dict = {}
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    if "is_inherited" in value:
        out["isInherited"] = value["is_inherited"]
    return out


def deserialize_json(data: dict) -> CompositeComponentTypeResponse:
    out: CompositeComponentTypeResponse = {}  # type: ignore[typeddict-item]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    if "isInherited" in data:
        out["is_inherited"] = data["isInherited"]
    return out
