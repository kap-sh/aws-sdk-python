"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_id


class CompositeComponentTypeRequest(TypedDict, closed=True):
    component_type_id: NotRequired[
        "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
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
