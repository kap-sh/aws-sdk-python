"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.voice_connector_group_name
    import aws_sdk_chime_sdk_voice.types.voice_connector_item_list


class UpdateVoiceConnectorGroupRequest(TypedDict, closed=True):
    voice_connector_group_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The Voice Connector ID.</p>"""
    name: "aws_sdk_chime_sdk_voice.types.voice_connector_group_name.VoiceConnectorGroupName"
    """<p>The name of the Voice Connector group.</p>"""
    voice_connector_items: (
        "aws_sdk_chime_sdk_voice.types.voice_connector_item_list.VoiceConnectorItemList"
    )
    """<p>The <code>VoiceConnectorItems</code> to associate with the Voice Connector group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_chime_sdk_voice.types.voice_connector_item_list

    out["VoiceConnectorItems"] = (
        aws_sdk_chime_sdk_voice.types.voice_connector_item_list.serialize_json(
            value["voice_connector_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateVoiceConnectorGroupRequest:
    out: UpdateVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateVoiceConnectorGroupRequest.name required")
    if "VoiceConnectorItems" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_item_list

        out["voice_connector_items"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_item_list.deserialize_json(
                data["VoiceConnectorItems"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateVoiceConnectorGroupRequest.voice_connector_items required"
        )
    return out
