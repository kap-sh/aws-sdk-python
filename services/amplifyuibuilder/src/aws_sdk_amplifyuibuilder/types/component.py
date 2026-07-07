"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Component``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

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
    import aws_sdk_amplifyuibuilder.types.uuid


class Component(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the component.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    source_id: NotRequired["str"]
    """<p>The unique ID of the component in its original source system, such as Figma.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the component.</p>"""
    name: "aws_sdk_amplifyuibuilder.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    component_type: "aws_sdk_amplifyuibuilder.types.component_type.ComponentType"
    """<p>The type of the component. This can be an Amplify custom UI component or another custom component.</p>"""
    properties: (
        "aws_sdk_amplifyuibuilder.types.component_properties.ComponentProperties"
    )
    """<p>Describes the component's properties. You can't specify <code>tags</code> as a valid property for <code>properties</code>.</p>"""
    children: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_child_list.ComponentChildList"
    ]
    """<p>A list of the component's <code>ComponentChild</code> instances.</p>"""
    variants: "aws_sdk_amplifyuibuilder.types.component_variants.ComponentVariants"
    """<p>A list of the component's variants. A variant is a unique style configuration of a main component.</p>"""
    overrides: "aws_sdk_amplifyuibuilder.types.component_overrides.ComponentOverrides"
    """<p>Describes the component's properties that can be overriden in a customized instance of the component. You can't specify <code>tags</code> as a valid property for <code>overrides</code>.</p>"""
    binding_properties: "aws_sdk_amplifyuibuilder.types.component_binding_properties.ComponentBindingProperties"
    """<p>The information to connect a component's properties to data at runtime. You can't specify <code>tags</code> as a valid property for <code>bindingProperties</code>.</p> <p/>"""
    collection_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_collection_properties.ComponentCollectionProperties"
    ]
    """<p>The data binding configuration for the component's properties. Use this for a collection component. You can't specify <code>tags</code> as a valid property for <code>collectionProperties</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The time that the component was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the component was modified.</p>"""
    tags: NotRequired["aws_sdk_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the component.</p>"""
    events: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_events.ComponentEvents"
    ]
    """<p>Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.</p>"""
    schema_version: NotRequired["str"]
    """<p>The schema version of the component when it was imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Component) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
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
    import aws_sdk_amplifyuibuilder.types._prelude.timestamp

    out["createdAt"] = aws_sdk_amplifyuibuilder.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "modified_at" in value:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["modifiedAt"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["modified_at"]
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


def deserialize_json(data: dict) -> Component:
    out: Component = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("Component.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("Component.environment_name required")
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Component.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Component.name required")
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("Component.component_type required")
    if "properties" in data:
        import aws_sdk_amplifyuibuilder.types.component_properties

        out["properties"] = (
            aws_sdk_amplifyuibuilder.types.component_properties.deserialize_json(
                data["properties"]
            )
        )
    else:
        raise DeserializationError("Component.properties required")
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
        raise DeserializationError("Component.variants required")
    if "overrides" in data:
        import aws_sdk_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.component_overrides.deserialize_json(
                data["overrides"]
            )
        )
    else:
        raise DeserializationError("Component.overrides required")
    if "bindingProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_binding_properties

        out["binding_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    else:
        raise DeserializationError("Component.binding_properties required")
    if "collectionProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_collection_properties

        out["collection_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_collection_properties.deserialize_json(
                data["collectionProperties"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Component.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_amplifyuibuilder.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
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
