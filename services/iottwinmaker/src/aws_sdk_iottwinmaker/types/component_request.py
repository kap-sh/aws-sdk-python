"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_property_group_requests
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.property_requests


class ComponentRequest(TypedDict, closed=True):
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component request.</p>"""
    component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>The ID of the component type.</p>"""
    properties: NotRequired[
        "aws_sdk_iottwinmaker.types.property_requests.PropertyRequests"
    ]
    """<p>An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.</p>"""
    property_groups: NotRequired[
        "aws_sdk_iottwinmaker.types.component_property_group_requests.ComponentPropertyGroupRequests"
    ]
    """<p>The property groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    if "properties" in value:
        import aws_sdk_iottwinmaker.types.property_requests

        out["properties"] = aws_sdk_iottwinmaker.types.property_requests.serialize_json(
            value["properties"]
        )
    if "property_groups" in value:
        import aws_sdk_iottwinmaker.types.component_property_group_requests

        out["propertyGroups"] = (
            aws_sdk_iottwinmaker.types.component_property_group_requests.serialize_json(
                value["property_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentRequest:
    out: ComponentRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    if "properties" in data:
        import aws_sdk_iottwinmaker.types.property_requests

        out["properties"] = (
            aws_sdk_iottwinmaker.types.property_requests.deserialize_json(
                data["properties"]
            )
        )
    if "propertyGroups" in data:
        import aws_sdk_iottwinmaker.types.component_property_group_requests

        out["property_groups"] = (
            aws_sdk_iottwinmaker.types.component_property_group_requests.deserialize_json(
                data["propertyGroups"]
            )
        )
    return out
