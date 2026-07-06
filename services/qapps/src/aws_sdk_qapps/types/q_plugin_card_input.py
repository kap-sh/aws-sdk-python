"""Generated from Smithy shape ``com.amazonaws.qapps#QPluginCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.action_identifier
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.plugin_id
    import aws_sdk_qapps.types.prompt
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class QPluginCardInput(TypedDict, closed=True):
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title or label of the plugin card.</p>"""
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the plugin card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    prompt: "aws_sdk_qapps.types.prompt.Prompt"
    """<p>The prompt or instructions displayed for the plugin card.</p>"""
    plugin_id: "aws_sdk_qapps.types.plugin_id.PluginId"
    """<p>The unique identifier of the plugin used by the card.</p>"""
    action_identifier: NotRequired[
        "aws_sdk_qapps.types.action_identifier.ActionIdentifier"
    ]
    """<p>The action identifier of the action to be performed by the plugin card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QPluginCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(
        value.get("type", "q-plugin")
    )
    out["prompt"] = value["prompt"]
    out["pluginId"] = value["plugin_id"]
    if "action_identifier" in value:
        out["actionIdentifier"] = value["action_identifier"]
    return out


def deserialize_json(data: dict) -> QPluginCardInput:
    out: QPluginCardInput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("QPluginCardInput.title required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("QPluginCardInput.id required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "q-plugin"
    if "prompt" in data:
        out["prompt"] = data["prompt"]
    else:
        raise DeserializationError("QPluginCardInput.prompt required")
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    else:
        raise DeserializationError("QPluginCardInput.plugin_id required")
    if "actionIdentifier" in data:
        out["action_identifier"] = data["actionIdentifier"]
    return out
