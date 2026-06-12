"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateComponentTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.component_type_name
    import aws_sdk_iottwinmaker.types.composite_component_types_request
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.extends_from
    import aws_sdk_iottwinmaker.types.functions_request
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.property_definitions_request
    import aws_sdk_iottwinmaker.types.property_groups_request
    import aws_sdk_iottwinmaker.types.tag_map


class CreateComponentTypeRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the component type.</p>"""
    is_singleton: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>"""
    component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    property_definitions: NotRequired[
        "aws_sdk_iottwinmaker.types.property_definitions_request.PropertyDefinitionsRequest"
    ]
    """<p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>"""
    extends_from: NotRequired["aws_sdk_iottwinmaker.types.extends_from.ExtendsFrom"]
    """<p>Specifies the parent component type to extend.</p>"""
    functions: NotRequired[
        "aws_sdk_iottwinmaker.types.functions_request.FunctionsRequest"
    ]
    """<p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>"""
    tags: NotRequired["aws_sdk_iottwinmaker.types.tag_map.TagMap"]
    """<p>Metadata that you can use to manage the component type.</p>"""
    property_groups: NotRequired[
        "aws_sdk_iottwinmaker.types.property_groups_request.PropertyGroupsRequest"
    ]
    """<p/>"""
    component_type_name: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_name.ComponentTypeName"
    ]
    """<p>A friendly name for the component type.</p>"""
    composite_component_types: NotRequired[
        "aws_sdk_iottwinmaker.types.composite_component_types_request.CompositeComponentTypesRequest"
    ]
    """<p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentTypeRequest) -> dict:
    out: dict = {}
    if "is_singleton" in value:
        out["isSingleton"] = value["is_singleton"]
    if "description" in value:
        out["description"] = value["description"]
    if "property_definitions" in value:
        import aws_sdk_iottwinmaker.types.property_definitions_request

        out["propertyDefinitions"] = (
            aws_sdk_iottwinmaker.types.property_definitions_request.serialize_json(
                value["property_definitions"]
            )
        )
    if "extends_from" in value:
        import aws_sdk_iottwinmaker.types.extends_from

        out["extendsFrom"] = aws_sdk_iottwinmaker.types.extends_from.serialize_json(
            value["extends_from"]
        )
    if "functions" in value:
        import aws_sdk_iottwinmaker.types.functions_request

        out["functions"] = aws_sdk_iottwinmaker.types.functions_request.serialize_json(
            value["functions"]
        )
    if "tags" in value:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    if "property_groups" in value:
        import aws_sdk_iottwinmaker.types.property_groups_request

        out["propertyGroups"] = (
            aws_sdk_iottwinmaker.types.property_groups_request.serialize_json(
                value["property_groups"]
            )
        )
    if "component_type_name" in value:
        out["componentTypeName"] = value["component_type_name"]
    if "composite_component_types" in value:
        import aws_sdk_iottwinmaker.types.composite_component_types_request

        out["compositeComponentTypes"] = (
            aws_sdk_iottwinmaker.types.composite_component_types_request.serialize_json(
                value["composite_component_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateComponentTypeRequest:
    out: CreateComponentTypeRequest = {}  # type: ignore[typeddict-item]
    if "isSingleton" in data:
        out["is_singleton"] = data["isSingleton"]
    if "description" in data:
        out["description"] = data["description"]
    if "propertyDefinitions" in data:
        import aws_sdk_iottwinmaker.types.property_definitions_request

        out["property_definitions"] = (
            aws_sdk_iottwinmaker.types.property_definitions_request.deserialize_json(
                data["propertyDefinitions"]
            )
        )
    if "extendsFrom" in data:
        import aws_sdk_iottwinmaker.types.extends_from

        out["extends_from"] = aws_sdk_iottwinmaker.types.extends_from.deserialize_json(
            data["extendsFrom"]
        )
    if "functions" in data:
        import aws_sdk_iottwinmaker.types.functions_request

        out["functions"] = (
            aws_sdk_iottwinmaker.types.functions_request.deserialize_json(
                data["functions"]
            )
        )
    if "tags" in data:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    if "propertyGroups" in data:
        import aws_sdk_iottwinmaker.types.property_groups_request

        out["property_groups"] = (
            aws_sdk_iottwinmaker.types.property_groups_request.deserialize_json(
                data["propertyGroups"]
            )
        )
    if "componentTypeName" in data:
        out["component_type_name"] = data["componentTypeName"]
    if "compositeComponentTypes" in data:
        import aws_sdk_iottwinmaker.types.composite_component_types_request

        out["composite_component_types"] = (
            aws_sdk_iottwinmaker.types.composite_component_types_request.deserialize_json(
                data["compositeComponentTypes"]
            )
        )
    return out
