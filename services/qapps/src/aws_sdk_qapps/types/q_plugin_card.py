"""Generated from Smithy shape ``com.amazonaws.qapps#QPluginCard``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.action_identifier
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.dependency_list
    import aws_sdk_qapps.types.plugin_type
    import aws_sdk_qapps.types.prompt
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class QPluginCard(TypedDict):
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the plugin card.</p>"""
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title or label of the plugin card.</p>"""
    dependencies: "aws_sdk_qapps.types.dependency_list.DependencyList"
    """<p>Any dependencies or requirements for the plugin card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    prompt: "aws_sdk_qapps.types.prompt.Prompt"
    """<p>The prompt or instructions displayed for the plugin card.</p>"""
    plugin_type: "aws_sdk_qapps.types.plugin_type.PluginType"
    """<p>The type or category of the plugin used by the card.</p>"""
    plugin_id: "str"
    """<p>The unique identifier of the plugin used by the card.</p>"""
    action_identifier: NotRequired[
        "aws_sdk_qapps.types.action_identifier.ActionIdentifier"
    ]
    """<p>The action identifier of the action to be performed by the plugin card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QPluginCard) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    import aws_sdk_qapps.types.dependency_list

    out["dependencies"] = aws_sdk_qapps.types.dependency_list.serialize_json(
        value["dependencies"]
    )
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(value["type"])
    out["prompt"] = value["prompt"]
    import aws_sdk_qapps.types.plugin_type

    out["pluginType"] = aws_sdk_qapps.types.plugin_type.serialize_json(
        value["plugin_type"]
    )
    out["pluginId"] = value["plugin_id"]
    if "action_identifier" in value:
        out["actionIdentifier"] = value["action_identifier"]
    return out


def deserialize_json(data: dict) -> QPluginCard:
    out: QPluginCard = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("QPluginCard.id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("QPluginCard.title required")
    if "dependencies" in data:
        import aws_sdk_qapps.types.dependency_list

        out["dependencies"] = aws_sdk_qapps.types.dependency_list.deserialize_json(
            data["dependencies"]
        )
    else:
        raise DeserializationError("QPluginCard.dependencies required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("QPluginCard.type required")
    if "prompt" in data:
        out["prompt"] = data["prompt"]
    else:
        raise DeserializationError("QPluginCard.prompt required")
    if "pluginType" in data:
        import aws_sdk_qapps.types.plugin_type

        out["plugin_type"] = aws_sdk_qapps.types.plugin_type.deserialize_json(
            data["pluginType"]
        )
    else:
        raise DeserializationError("QPluginCard.plugin_type required")
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    else:
        raise DeserializationError("QPluginCard.plugin_id required")
    if "actionIdentifier" in data:
        out["action_identifier"] = data["actionIdentifier"]
    return out
