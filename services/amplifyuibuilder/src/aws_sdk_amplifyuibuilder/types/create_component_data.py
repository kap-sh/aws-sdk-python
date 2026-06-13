"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateComponentData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_binding_properties
    import aws_sdk_amplifyuibuilder.types.component_child_list
    import aws_sdk_amplifyuibuilder.types.component_collection_properties
    import aws_sdk_amplifyuibuilder.types.component_events
    import aws_sdk_amplifyuibuilder.types.component_name
    import aws_sdk_amplifyuibuilder.types.component_overrides
    import aws_sdk_amplifyuibuilder.types.component_properties
    import aws_sdk_amplifyuibuilder.types.component_type
    import aws_sdk_amplifyuibuilder.types.component_variants
    import aws_sdk_amplifyuibuilder.types.tags


class CreateComponentData(TypedDict):
    name: "aws_sdk_amplifyuibuilder.types.component_name.ComponentName"
    """<p>The name of the component</p>"""
    source_id: NotRequired["str"]
    """<p>The unique ID of the component in its original source system, such as Figma.</p>"""
    component_type: "aws_sdk_amplifyuibuilder.types.component_type.ComponentType"
    """<p>The component type. This can be an Amplify custom UI component or another custom component.</p>"""
    properties: (
        "aws_sdk_amplifyuibuilder.types.component_properties.ComponentProperties"
    )
    """<p>Describes the component's properties.</p>"""
    children: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_child_list.ComponentChildList"
    ]
    """<p>A list of child components that are instances of the main component.</p>"""
    variants: "aws_sdk_amplifyuibuilder.types.component_variants.ComponentVariants"
    """<p>A list of the unique variants of this component.</p>"""
    overrides: "aws_sdk_amplifyuibuilder.types.component_overrides.ComponentOverrides"
    """<p>Describes the component properties that can be overriden to customize an instance of the component.</p>"""
    binding_properties: "aws_sdk_amplifyuibuilder.types.component_binding_properties.ComponentBindingProperties"
    """<p>The data binding information for the component's properties.</p>"""
    collection_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_collection_properties.ComponentCollectionProperties"
    ]
    """<p>The data binding configuration for customizing a component's properties. Use this for a collection component.</p>"""
    tags: NotRequired["aws_sdk_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the component data.</p>"""
    events: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_events.ComponentEvents"
    ]
    """<p>The event configuration for the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.</p>"""
    schema_version: NotRequired["str"]
    """<p>The schema version of the component when it was imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentData) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    out["componentType"] = value["component_type"]
    import aws_sdk_amplifyuibuilder.types.component_properties

    out["properties"] = (
        aws_sdk_amplifyuibuilder.types.component_properties.serialize_json(
            value["properties"]
        )
    )
    if "children" in value:
        import aws_sdk_amplifyuibuilder.types.component_child_list

        out["children"] = (
            aws_sdk_amplifyuibuilder.types.component_child_list.serialize_json(
                value["children"]
            )
        )
    import aws_sdk_amplifyuibuilder.types.component_variants

    out["variants"] = aws_sdk_amplifyuibuilder.types.component_variants.serialize_json(
        value["variants"]
    )
    import aws_sdk_amplifyuibuilder.types.component_overrides

    out["overrides"] = (
        aws_sdk_amplifyuibuilder.types.component_overrides.serialize_json(
            value["overrides"]
        )
    )
    import aws_sdk_amplifyuibuilder.types.component_binding_properties

    out["bindingProperties"] = (
        aws_sdk_amplifyuibuilder.types.component_binding_properties.serialize_json(
            value["binding_properties"]
        )
    )
    if "collection_properties" in value:
        import aws_sdk_amplifyuibuilder.types.component_collection_properties

        out["collectionProperties"] = (
            aws_sdk_amplifyuibuilder.types.component_collection_properties.serialize_json(
                value["collection_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "events" in value:
        import aws_sdk_amplifyuibuilder.types.component_events

        out["events"] = aws_sdk_amplifyuibuilder.types.component_events.serialize_json(
            value["events"]
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    return out


def deserialize_json(data: dict) -> CreateComponentData:
    out: CreateComponentData = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateComponentData.name required")
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("CreateComponentData.component_type required")
    if "properties" in data:
        import aws_sdk_amplifyuibuilder.types.component_properties

        out["properties"] = (
            aws_sdk_amplifyuibuilder.types.component_properties.deserialize_json(
                data["properties"]
            )
        )
    else:
        raise DeserializationError("CreateComponentData.properties required")
    if "children" in data:
        import aws_sdk_amplifyuibuilder.types.component_child_list

        out["children"] = (
            aws_sdk_amplifyuibuilder.types.component_child_list.deserialize_json(
                data["children"]
            )
        )
    if "variants" in data:
        import aws_sdk_amplifyuibuilder.types.component_variants

        out["variants"] = (
            aws_sdk_amplifyuibuilder.types.component_variants.deserialize_json(
                data["variants"]
            )
        )
    else:
        raise DeserializationError("CreateComponentData.variants required")
    if "overrides" in data:
        import aws_sdk_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.component_overrides.deserialize_json(
                data["overrides"]
            )
        )
    else:
        raise DeserializationError("CreateComponentData.overrides required")
    if "bindingProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_binding_properties

        out["binding_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    else:
        raise DeserializationError("CreateComponentData.binding_properties required")
    if "collectionProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_collection_properties

        out["collection_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_collection_properties.deserialize_json(
                data["collectionProperties"]
            )
        )
    if "tags" in data:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if "events" in data:
        import aws_sdk_amplifyuibuilder.types.component_events

        out["events"] = (
            aws_sdk_amplifyuibuilder.types.component_events.deserialize_json(
                data["events"]
            )
        )
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    return out
