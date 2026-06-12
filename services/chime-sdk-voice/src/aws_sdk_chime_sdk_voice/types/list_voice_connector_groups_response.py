"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceConnectorGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.voice_connector_group_list


class ListVoiceConnectorGroupsResponse(TypedDict):
    voice_connector_groups: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_group_list.VoiceConnectorGroupList"
    ]
    """<p>The details of the Voice Connector groups.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceConnectorGroupsResponse) -> dict:
    out: dict = {}
    if "voice_connector_groups" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_group_list

        out["VoiceConnectorGroups"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_group_list.serialize_json(
                value["voice_connector_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVoiceConnectorGroupsResponse:
    out: ListVoiceConnectorGroupsResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorGroups" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_group_list

        out["voice_connector_groups"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_group_list.deserialize_json(
                data["VoiceConnectorGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
