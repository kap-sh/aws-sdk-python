"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.component_property_group_responses
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.composite_component_response
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.property_responses
    import aws_sdk_iottwinmaker.types.status
    import aws_sdk_iottwinmaker.types.string
    import aws_sdk_iottwinmaker.types.sync_source


class ComponentResponse(TypedDict, closed=True):
    component_name: NotRequired["aws_sdk_iottwinmaker.types.name.Name"]
    """<p>The name of the component.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>The ID of the component type.</p>"""
    status: NotRequired["aws_sdk_iottwinmaker.types.status.Status"]
    """<p>The status of the component type.</p>"""
    defined_in: NotRequired["aws_sdk_iottwinmaker.types.string.String"]
    """<p>The name of the property definition set in the request.</p>"""
    properties: NotRequired[
        "aws_sdk_iottwinmaker.types.property_responses.PropertyResponses"
    ]
    """<p>An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.</p>"""
    property_groups: NotRequired[
        "aws_sdk_iottwinmaker.types.component_property_group_responses.ComponentPropertyGroupResponses"
    ]
    """<p>The property groups.</p>"""
    sync_source: NotRequired["aws_sdk_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The syncSource of the sync job, if this entity was created by a sync job.</p>"""
    are_all_properties_returned: NotRequired[
        "aws_sdk_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all properties of the component are returned in the API response. The maximum number of properties returned is 800.</p>"""
    composite_components: NotRequired[
        "aws_sdk_iottwinmaker.types.composite_component_response.CompositeComponentResponse"
    ]
    """<p>This lists objects that contain information about the <code>compositeComponents</code>.</p>"""
    are_all_composite_components_returned: NotRequired[
        "aws_sdk_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all <code>compositeComponents</code> are returned in the API response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentResponse) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    if "status" in value:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.serialize_json(
            value["status"]
        )
    if "defined_in" in value:
        out["definedIn"] = value["defined_in"]
    if "properties" in value:
        import aws_sdk_iottwinmaker.types.property_responses

        out["properties"] = (
            aws_sdk_iottwinmaker.types.property_responses.serialize_json(
                value["properties"]
            )
        )
    if "property_groups" in value:
        import aws_sdk_iottwinmaker.types.component_property_group_responses

        out["propertyGroups"] = (
            aws_sdk_iottwinmaker.types.component_property_group_responses.serialize_json(
                value["property_groups"]
            )
        )
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "are_all_properties_returned" in value:
        out["areAllPropertiesReturned"] = value["are_all_properties_returned"]
    if "composite_components" in value:
        import aws_sdk_iottwinmaker.types.composite_component_response

        out["compositeComponents"] = (
            aws_sdk_iottwinmaker.types.composite_component_response.serialize_json(
                value["composite_components"]
            )
        )
    if "are_all_composite_components_returned" in value:
        out["areAllCompositeComponentsReturned"] = value[
            "are_all_composite_components_returned"
        ]
    return out


def deserialize_json(data: dict) -> ComponentResponse:
    out: ComponentResponse = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "description" in data:
        out["description"] = data["description"]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    if "status" in data:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.deserialize_json(
            data["status"]
        )
    if "definedIn" in data:
        out["defined_in"] = data["definedIn"]
    if "properties" in data:
        import aws_sdk_iottwinmaker.types.property_responses

        out["properties"] = (
            aws_sdk_iottwinmaker.types.property_responses.deserialize_json(
                data["properties"]
            )
        )
    if "propertyGroups" in data:
        import aws_sdk_iottwinmaker.types.component_property_group_responses

        out["property_groups"] = (
            aws_sdk_iottwinmaker.types.component_property_group_responses.deserialize_json(
                data["propertyGroups"]
            )
        )
    if "syncSource" in data:
        out["sync_source"] = data["syncSource"]
    if "areAllPropertiesReturned" in data:
        out["are_all_properties_returned"] = data["areAllPropertiesReturned"]
    if "compositeComponents" in data:
        import aws_sdk_iottwinmaker.types.composite_component_response

        out["composite_components"] = (
            aws_sdk_iottwinmaker.types.composite_component_response.deserialize_json(
                data["compositeComponents"]
            )
        )
    if "areAllCompositeComponentsReturned" in data:
        out["are_all_composite_components_returned"] = data[
            "areAllCompositeComponentsReturned"
        ]
    return out
