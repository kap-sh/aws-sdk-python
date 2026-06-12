"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPropertyValueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.selected_property_list
    import aws_sdk_iottwinmaker.types.tabular_conditions


class GetPropertyValueRequest(TypedDict):
    component_name: NotRequired["aws_sdk_iottwinmaker.types.name.Name"]
    """<p>The name of the component whose property values the operation returns.</p>"""
    component_path: NotRequired[
        "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
    ]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>The ID of the component type whose property values the operation returns.</p>"""
    entity_id: NotRequired["aws_sdk_iottwinmaker.types.entity_id.EntityId"]
    """<p>The ID of the entity whose property values the operation returns.</p>"""
    selected_properties: (
        "aws_sdk_iottwinmaker.types.selected_property_list.SelectedPropertyList"
    )
    """<p>The properties whose values the operation returns.</p>"""
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace whose values the operation returns.</p>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    property_group_name: NotRequired["aws_sdk_iottwinmaker.types.name.Name"]
    """<p>The property group name.</p>"""
    tabular_conditions: NotRequired[
        "aws_sdk_iottwinmaker.types.tabular_conditions.TabularConditions"
    ]
    """<p>The tabular conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertyValueRequest) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    import aws_sdk_iottwinmaker.types.selected_property_list

    out["selectedProperties"] = (
        aws_sdk_iottwinmaker.types.selected_property_list.serialize_json(
            value["selected_properties"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "property_group_name" in value:
        out["propertyGroupName"] = value["property_group_name"]
    if "tabular_conditions" in value:
        import aws_sdk_iottwinmaker.types.tabular_conditions

        out["tabularConditions"] = (
            aws_sdk_iottwinmaker.types.tabular_conditions.serialize_json(
                value["tabular_conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPropertyValueRequest:
    out: GetPropertyValueRequest = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentPath" in data:
        out["component_path"] = data["componentPath"]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "selectedProperties" in data:
        import aws_sdk_iottwinmaker.types.selected_property_list

        out["selected_properties"] = (
            aws_sdk_iottwinmaker.types.selected_property_list.deserialize_json(
                data["selectedProperties"]
            )
        )
    else:
        raise DeserializationError(
            "GetPropertyValueRequest.selected_properties required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "propertyGroupName" in data:
        out["property_group_name"] = data["propertyGroupName"]
    if "tabularConditions" in data:
        import aws_sdk_iottwinmaker.types.tabular_conditions

        out["tabular_conditions"] = (
            aws_sdk_iottwinmaker.types.tabular_conditions.deserialize_json(
                data["tabularConditions"]
            )
        )
    return out
