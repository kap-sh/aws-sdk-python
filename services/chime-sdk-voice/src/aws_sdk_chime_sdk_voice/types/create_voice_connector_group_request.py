"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_connector_group_name
    import aws_sdk_chime_sdk_voice.types.voice_connector_item_list


class CreateVoiceConnectorGroupRequest(TypedDict, closed=True):
    name: "aws_sdk_chime_sdk_voice.types.voice_connector_group_name.VoiceConnectorGroupName"
    """<p>The name of the Voice Connector group.</p>"""
    voice_connector_items: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_item_list.VoiceConnectorItemList"
    ]
    """<p>Lists the Voice Connectors that inbound calls are routed to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "voice_connector_items" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_item_list

        out["VoiceConnectorItems"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_item_list.serialize_json(
                value["voice_connector_items"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateVoiceConnectorGroupRequest:
    out: CreateVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateVoiceConnectorGroupRequest.name required")
    if "VoiceConnectorItems" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_item_list

        out["voice_connector_items"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_item_list.deserialize_json(
                data["VoiceConnectorItems"]
            )
        )
    return out
