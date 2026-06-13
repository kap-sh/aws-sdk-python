"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateComponentData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

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
    import aws_sdk_amplifyuibuilder.types.uuid


class UpdateComponentData(TypedDict):
    id: NotRequired["aws_sdk_amplifyuibuilder.types.uuid.Uuid"]
    """<p>The unique ID of the component to update.</p>"""
    name: NotRequired["aws_sdk_amplifyuibuilder.types.component_name.ComponentName"]
    """<p>The name of the component to update.</p>"""
    source_id: NotRequired["str"]
    """<p>The unique ID of the component in its original source system, such as Figma.</p>"""
    component_type: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_type.ComponentType"
    ]
    """<p>The type of the component. This can be an Amplify custom UI component or another custom component.</p>"""
    properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_properties.ComponentProperties"
    ]
    """<p>Describes the component's properties.</p>"""
    children: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_child_list.ComponentChildList"
    ]
    """<p>The components that are instances of the main component.</p>"""
    variants: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_variants.ComponentVariants"
    ]
    """<p>A list of the unique variants of the main component being updated.</p>"""
    overrides: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_overrides.ComponentOverrides"
    ]
    """<p>Describes the properties that can be overriden to customize the component.</p>"""
    binding_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_binding_properties.ComponentBindingProperties"
    ]
    """<p>The data binding information for the component's properties.</p>"""
    collection_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_collection_properties.ComponentCollectionProperties"
    ]
    """<p>The configuration for binding a component's properties to a data model. Use this for a collection component.</p>"""
    events: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_events.ComponentEvents"
    ]
    """<p>The event configuration for the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.</p>"""
    schema_version: NotRequired["str"]
    """<p>The schema version of the component when it was imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComponentData) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "component_type" in value:
        out["componentType"] = value["component_type"]
    if "properties" in value:
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
    if "variants" in value:
        import aws_sdk_amplifyuibuilder.types.component_variants

        out["variants"] = (
            aws_sdk_amplifyuibuilder.types.component_variants.serialize_json(
                value["variants"]
            )
        )
    if "overrides" in value:
        import aws_sdk_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.component_overrides.serialize_json(
                value["overrides"]
            )
        )
    if "binding_properties" in value:
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
    if "events" in value:
        import aws_sdk_amplifyuibuilder.types.component_events

        out["events"] = aws_sdk_amplifyuibuilder.types.component_events.serialize_json(
            value["events"]
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    return out


def deserialize_json(data: dict) -> UpdateComponentData:
    out: UpdateComponentData = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    if "properties" in data:
        import aws_sdk_amplifyuibuilder.types.component_properties

        out["properties"] = (
            aws_sdk_amplifyuibuilder.types.component_properties.deserialize_json(
                data["properties"]
            )
        )
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
    if "overrides" in data:
        import aws_sdk_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.component_overrides.deserialize_json(
                data["overrides"]
            )
        )
    if "bindingProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_binding_properties

        out["binding_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    if "collectionProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_collection_properties

        out["collection_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_collection_properties.deserialize_json(
                data["collectionProperties"]
            )
        )
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
