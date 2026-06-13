"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentChild``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_child_list
    import aws_sdk_amplifyuibuilder.types.component_events
    import aws_sdk_amplifyuibuilder.types.component_properties


class ComponentChild(TypedDict):
    component_type: "str"
    """<p>The type of the child component. </p>"""
    name: "str"
    """<p>The name of the child component.</p>"""
    properties: (
        "aws_sdk_amplifyuibuilder.types.component_properties.ComponentProperties"
    )
    """<p>Describes the properties of the child component. You can't specify <code>tags</code> as a valid property for <code>properties</code>.</p>"""
    children: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_child_list.ComponentChildList"
    ]
    """<p>The list of <code>ComponentChild</code> instances for this component.</p>"""
    events: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_events.ComponentEvents"
    ]
    """<p>Describes the events that can be raised on the child component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.</p>"""
    source_id: NotRequired["str"]
    """<p>The unique ID of the child component in its original source system, such as Figma.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentChild) -> dict:
    out: dict = {}
    out["componentType"] = value["component_type"]
    out["name"] = value["name"]
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
    if "events" in value:
        import aws_sdk_amplifyuibuilder.types.component_events

        out["events"] = aws_sdk_amplifyuibuilder.types.component_events.serialize_json(
            value["events"]
        )
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    return out


def deserialize_json(data: dict) -> ComponentChild:
    out: ComponentChild = {}  # type: ignore[typeddict-item]
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("ComponentChild.component_type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComponentChild.name required")
    if "properties" in data:
        import aws_sdk_amplifyuibuilder.types.component_properties

        out["properties"] = (
            aws_sdk_amplifyuibuilder.types.component_properties.deserialize_json(
                data["properties"]
            )
        )
    else:
        raise DeserializationError("ComponentChild.properties required")
    if "children" in data:
        import aws_sdk_amplifyuibuilder.types.component_child_list

        out["children"] = (
            aws_sdk_amplifyuibuilder.types.component_child_list.deserialize_json(
                data["children"]
            )
        )
    if "events" in data:
        import aws_sdk_amplifyuibuilder.types.component_events

        out["events"] = (
            aws_sdk_amplifyuibuilder.types.component_events.deserialize_json(
                data["events"]
            )
        )
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    return out
