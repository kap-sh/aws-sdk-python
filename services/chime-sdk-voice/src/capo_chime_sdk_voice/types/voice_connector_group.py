"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.voice_connector_group_name
    import capo_chime_sdk_voice.types.voice_connector_item_list


class VoiceConnectorGroup(TypedDict, closed=True):
    voice_connector_group_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of a Voice Connector group.</p>"""
    name: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_group_name.VoiceConnectorGroupName"
    ]
    """<p>The name of a Voice Connector group.</p>"""
    voice_connector_items: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_item_list.VoiceConnectorItemList"
    ]
    """<p>The Voice Connectors to which you route inbound calls.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The Voice Connector group's creation time stamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The Voice Connector group's creation time stamp, in ISO 8601 format.</p>"""
    voice_connector_group_arn: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Voice Connector group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorGroup) -> dict:
    out: dict = {}
    if "voice_connector_group_id" in value:
        out["VoiceConnectorGroupId"] = value["voice_connector_group_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "voice_connector_items" in value:
        import capo_chime_sdk_voice.types.voice_connector_item_list

        out["VoiceConnectorItems"] = (
            capo_chime_sdk_voice.types.voice_connector_item_list.serialize_json(
                value["voice_connector_items"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "voice_connector_group_arn" in value:
        out["VoiceConnectorGroupArn"] = value["voice_connector_group_arn"]
    return out


def deserialize_json(data: dict) -> VoiceConnectorGroup:
    out: VoiceConnectorGroup = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorGroupId" in data:
        out["voice_connector_group_id"] = data["VoiceConnectorGroupId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VoiceConnectorItems" in data:
        import capo_chime_sdk_voice.types.voice_connector_item_list

        out["voice_connector_items"] = (
            capo_chime_sdk_voice.types.voice_connector_item_list.deserialize_json(
                data["VoiceConnectorItems"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "VoiceConnectorGroupArn" in data:
        out["voice_connector_group_arn"] = data["VoiceConnectorGroupArn"]
    return out
