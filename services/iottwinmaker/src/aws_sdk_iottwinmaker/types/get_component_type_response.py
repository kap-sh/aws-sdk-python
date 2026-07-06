"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetComponentTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.component_type_name
    import aws_sdk_iottwinmaker.types.composite_component_types_response
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.extends_from
    import aws_sdk_iottwinmaker.types.functions_response
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.property_definitions_response
    import aws_sdk_iottwinmaker.types.property_groups_response
    import aws_sdk_iottwinmaker.types.status
    import aws_sdk_iottwinmaker.types.sync_source
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class GetComponentTypeResponse(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the component type.</p>"""
    is_singleton: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>"""
    component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    property_definitions: NotRequired[
        "aws_sdk_iottwinmaker.types.property_definitions_response.PropertyDefinitionsResponse"
    ]
    """<p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>"""
    extends_from: NotRequired["aws_sdk_iottwinmaker.types.extends_from.ExtendsFrom"]
    """<p>The name of the parent component type that this component type extends.</p>"""
    functions: NotRequired[
        "aws_sdk_iottwinmaker.types.functions_response.FunctionsResponse"
    ]
    """<p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component type was created.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component was last updated.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the component type.</p>"""
    is_abstract: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the component type is abstract.</p>"""
    is_schema_initialized: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.</p>"""
    status: NotRequired["aws_sdk_iottwinmaker.types.status.Status"]
    """<p>The current status of the component type.</p>"""
    property_groups: NotRequired[
        "aws_sdk_iottwinmaker.types.property_groups_response.PropertyGroupsResponse"
    ]
    """<p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>"""
    sync_source: NotRequired["aws_sdk_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The syncSource of the SyncJob, if this entity was created by a SyncJob.</p>"""
    component_type_name: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_name.ComponentTypeName"
    ]
    """<p>The component type name.</p>"""
    composite_component_types: NotRequired[
        "aws_sdk_iottwinmaker.types.composite_component_types_response.CompositeComponentTypesResponse"
    ]
    """<p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentTypeResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    if "is_singleton" in value:
        out["isSingleton"] = value["is_singleton"]
    out["componentTypeId"] = value["component_type_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "property_definitions" in value:
        import aws_sdk_iottwinmaker.types.property_definitions_response

        out["propertyDefinitions"] = (
            aws_sdk_iottwinmaker.types.property_definitions_response.serialize_json(
                value["property_definitions"]
            )
        )
    if "extends_from" in value:
        import aws_sdk_iottwinmaker.types.extends_from

        out["extendsFrom"] = aws_sdk_iottwinmaker.types.extends_from.serialize_json(
            value["extends_from"]
        )
    if "functions" in value:
        import aws_sdk_iottwinmaker.types.functions_response

        out["functions"] = aws_sdk_iottwinmaker.types.functions_response.serialize_json(
            value["functions"]
        )
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    out["arn"] = value["arn"]
    if "is_abstract" in value:
        out["isAbstract"] = value["is_abstract"]
    if "is_schema_initialized" in value:
        out["isSchemaInitialized"] = value["is_schema_initialized"]
    if "status" in value:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.serialize_json(
            value["status"]
        )
    if "property_groups" in value:
        import aws_sdk_iottwinmaker.types.property_groups_response

        out["propertyGroups"] = (
            aws_sdk_iottwinmaker.types.property_groups_response.serialize_json(
                value["property_groups"]
            )
        )
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "component_type_name" in value:
        out["componentTypeName"] = value["component_type_name"]
    if "composite_component_types" in value:
        import aws_sdk_iottwinmaker.types.composite_component_types_response

        out["compositeComponentTypes"] = (
            aws_sdk_iottwinmaker.types.composite_component_types_response.serialize_json(
                value["composite_component_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetComponentTypeResponse:
    out: GetComponentTypeResponse = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("GetComponentTypeResponse.workspace_id required")
    if "isSingleton" in data:
        out["is_singleton"] = data["isSingleton"]
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    else:
        raise DeserializationError(
            "GetComponentTypeResponse.component_type_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "propertyDefinitions" in data:
        import aws_sdk_iottwinmaker.types.property_definitions_response

        out["property_definitions"] = (
            aws_sdk_iottwinmaker.types.property_definitions_response.deserialize_json(
                data["propertyDefinitions"]
            )
        )
    if "extendsFrom" in data:
        import aws_sdk_iottwinmaker.types.extends_from

        out["extends_from"] = aws_sdk_iottwinmaker.types.extends_from.deserialize_json(
            data["extendsFrom"]
        )
    if "functions" in data:
        import aws_sdk_iottwinmaker.types.functions_response

        out["functions"] = (
            aws_sdk_iottwinmaker.types.functions_response.deserialize_json(
                data["functions"]
            )
        )
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetComponentTypeResponse.creation_date_time required"
        )
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("GetComponentTypeResponse.update_date_time required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetComponentTypeResponse.arn required")
    if "isAbstract" in data:
        out["is_abstract"] = data["isAbstract"]
    if "isSchemaInitialized" in data:
        out["is_schema_initialized"] = data["isSchemaInitialized"]
    if "status" in data:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.deserialize_json(
            data["status"]
        )
    if "propertyGroups" in data:
        import aws_sdk_iottwinmaker.types.property_groups_response

        out["property_groups"] = (
            aws_sdk_iottwinmaker.types.property_groups_response.deserialize_json(
                data["propertyGroups"]
            )
        )
    if "syncSource" in data:
        out["sync_source"] = data["syncSource"]
    if "componentTypeName" in data:
        out["component_type_name"] = data["componentTypeName"]
    if "compositeComponentTypes" in data:
        import aws_sdk_iottwinmaker.types.composite_component_types_response

        out["composite_component_types"] = (
            aws_sdk_iottwinmaker.types.composite_component_types_response.deserialize_json(
                data["compositeComponentTypes"]
            )
        )
    return out
