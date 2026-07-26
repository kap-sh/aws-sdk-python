"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_property_group_requests
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.property_requests


class CompositeComponentRequest(TypedDict, closed=True):
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    properties: NotRequired[
        "capo_iottwinmaker.types.property_requests.PropertyRequests"
    ]
    """<p>This is an object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.</p>"""
    property_groups: NotRequired[
        "capo_iottwinmaker.types.component_property_group_requests.ComponentPropertyGroupRequests"
    ]
    """<p>The property groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeComponentRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "properties" in value:
        import capo_iottwinmaker.types.property_requests

        out["properties"] = capo_iottwinmaker.types.property_requests.serialize_json(
            value["properties"]
        )
    if "property_groups" in value:
        import capo_iottwinmaker.types.component_property_group_requests

        out["propertyGroups"] = (
            capo_iottwinmaker.types.component_property_group_requests.serialize_json(
                value["property_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> CompositeComponentRequest:
    out: CompositeComponentRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "properties" in data:
        import capo_iottwinmaker.types.property_requests

        out["properties"] = capo_iottwinmaker.types.property_requests.deserialize_json(
            data["properties"]
        )
    if "propertyGroups" in data:
        import capo_iottwinmaker.types.component_property_group_requests

        out["property_groups"] = (
            capo_iottwinmaker.types.component_property_group_requests.deserialize_json(
                data["propertyGroups"]
            )
        )
    return out
