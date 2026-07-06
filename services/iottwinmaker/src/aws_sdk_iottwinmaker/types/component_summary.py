"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_path
    import aws_sdk_iottwinmaker.types.component_property_group_responses
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.status
    import aws_sdk_iottwinmaker.types.string
    import aws_sdk_iottwinmaker.types.sync_source


class ComponentSummary(TypedDict, closed=True):
    component_name: "aws_sdk_iottwinmaker.types.name.Name"
    """<p>The name of the component.</p>"""
    component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    defined_in: NotRequired["aws_sdk_iottwinmaker.types.string.String"]
    """<p>The name of the property definition set in the request.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component request.</p>"""
    property_groups: NotRequired[
        "aws_sdk_iottwinmaker.types.component_property_group_responses.ComponentPropertyGroupResponses"
    ]
    """<p>The property groups.</p>"""
    status: "aws_sdk_iottwinmaker.types.status.Status"
    """<p>The status of the component type.</p>"""
    sync_source: NotRequired["aws_sdk_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The <code>syncSource</code> of the sync job, if this entity was created by a sync job.</p>"""
    component_path: NotRequired[
        "aws_sdk_iottwinmaker.types.component_path.ComponentPath"
    ]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummary) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    out["componentTypeId"] = value["component_type_id"]
    if "defined_in" in value:
        out["definedIn"] = value["defined_in"]
    if "description" in value:
        out["description"] = value["description"]
    if "property_groups" in value:
        import aws_sdk_iottwinmaker.types.component_property_group_responses

        out["propertyGroups"] = (
            aws_sdk_iottwinmaker.types.component_property_group_responses.serialize_json(
                value["property_groups"]
            )
        )
    import aws_sdk_iottwinmaker.types.status

    out["status"] = aws_sdk_iottwinmaker.types.status.serialize_json(value["status"])
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    return out


def deserialize_json(data: dict) -> ComponentSummary:
    out: ComponentSummary = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    else:
        raise DeserializationError("ComponentSummary.component_name required")
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    else:
        raise DeserializationError("ComponentSummary.component_type_id required")
    if "definedIn" in data:
        out["defined_in"] = data["definedIn"]
    if "description" in data:
        out["description"] = data["description"]
    if "propertyGroups" in data:
        import aws_sdk_iottwinmaker.types.component_property_group_responses

        out["property_groups"] = (
            aws_sdk_iottwinmaker.types.component_property_group_responses.deserialize_json(
                data["propertyGroups"]
            )
        )
    if "status" in data:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ComponentSummary.status required")
    if "syncSource" in data:
        out["sync_source"] = data["syncSource"]
    if "componentPath" in data:
        out["component_path"] = data["componentPath"]
    return out
