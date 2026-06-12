"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_id


class CompositeComponentTypeRequest(TypedDict):
    component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>This is the <code>componentTypeId</code> that the <code>compositeComponentType</code> refers to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeComponentTypeRequest) -> dict:
    out: dict = {}
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    return out


def deserialize_json(data: dict) -> CompositeComponentTypeRequest:
    out: CompositeComponentTypeRequest = {}  # type: ignore[typeddict-item]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    return out
