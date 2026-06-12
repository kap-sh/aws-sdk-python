"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_property_group_requests
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.component_update_type
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.property_requests


class ComponentUpdateRequest(TypedDict):
    update_type: NotRequired[
        "aws_sdk_iottwinmaker.types.component_update_type.ComponentUpdateType"
    ]
    """<p>The update type of the component update request.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>The ID of the component type.</p>"""
    property_updates: NotRequired[
        "aws_sdk_iottwinmaker.types.property_requests.PropertyRequests"
    ]
    """<p>An object that maps strings to the properties to set in the component type update. Each string in the mapping must be unique to this object.</p>"""
    property_group_updates: NotRequired[
        "aws_sdk_iottwinmaker.types.component_property_group_requests.ComponentPropertyGroupRequests"
    ]
    """<p>The property group updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentUpdateRequest) -> dict:
    out: dict = {}
    if "update_type" in value:
        out["updateType"] = value["update_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    if "property_updates" in value:
        import aws_sdk_iottwinmaker.types.property_requests

        out["propertyUpdates"] = (
            aws_sdk_iottwinmaker.types.property_requests.serialize_json(
                value["property_updates"]
            )
        )
    if "property_group_updates" in value:
        import aws_sdk_iottwinmaker.types.component_property_group_requests

        out["propertyGroupUpdates"] = (
            aws_sdk_iottwinmaker.types.component_property_group_requests.serialize_json(
                value["property_group_updates"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentUpdateRequest:
    out: ComponentUpdateRequest = {}  # type: ignore[typeddict-item]
    if "updateType" in data:
        out["update_type"] = data["updateType"]
    if "description" in data:
        out["description"] = data["description"]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    if "propertyUpdates" in data:
        import aws_sdk_iottwinmaker.types.property_requests

        out["property_updates"] = (
            aws_sdk_iottwinmaker.types.property_requests.deserialize_json(
                data["propertyUpdates"]
            )
        )
    if "propertyGroupUpdates" in data:
        import aws_sdk_iottwinmaker.types.component_property_group_requests

        out["property_group_updates"] = (
            aws_sdk_iottwinmaker.types.component_property_group_requests.deserialize_json(
                data["propertyGroupUpdates"]
            )
        )
    return out
