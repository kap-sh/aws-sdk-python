"""Generated from Smithy shape ``com.amazonaws.inspector2#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.component
    import capo_inspector2.types.component_arn
    import capo_inspector2.types.component_type


class Step(TypedDict, closed=True):
    component_id: "capo_inspector2.types.component.Component"
    """<p>The component ID.</p>"""
    component_type: "capo_inspector2.types.component_type.ComponentType"
    """<p>The component type.</p>"""
    component_arn: NotRequired["capo_inspector2.types.component_arn.ComponentArn"]
    """<p>The component ARN. The ARN can be null and is not displayed in the Amazon Web Services console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    out["componentId"] = value["component_id"]
    out["componentType"] = value["component_type"]
    if "component_arn" in value:
        out["componentArn"] = value["component_arn"]
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if "componentId" in data:
        out["component_id"] = data["componentId"]
    else:
        raise DeserializationError("Step.component_id required")
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("Step.component_type required")
    if "componentArn" in data:
        out["component_arn"] = data["componentArn"]
    return out
