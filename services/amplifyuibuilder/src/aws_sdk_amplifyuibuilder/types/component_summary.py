"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_name
    import aws_sdk_amplifyuibuilder.types.component_type
    import aws_sdk_amplifyuibuilder.types.uuid


class ComponentSummary(TypedDict):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the component.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the component.</p>"""
    name: "aws_sdk_amplifyuibuilder.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    component_type: "aws_sdk_amplifyuibuilder.types.component_type.ComponentType"
    """<p>The component type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["componentType"] = value["component_type"]
    return out


def deserialize_json(data: dict) -> ComponentSummary:
    out: ComponentSummary = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("ComponentSummary.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("ComponentSummary.environment_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ComponentSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComponentSummary.name required")
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("ComponentSummary.component_type required")
    return out
