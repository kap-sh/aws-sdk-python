"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceConnectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.voice_connector_list


class ListVoiceConnectorsResponse(TypedDict):
    voice_connectors: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_list.VoiceConnectorList"
    ]
    """<p>The details of the Voice Connectors.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceConnectorsResponse) -> dict:
    out: dict = {}
    if "voice_connectors" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_list

        out["VoiceConnectors"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_list.serialize_json(
                value["voice_connectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVoiceConnectorsResponse:
    out: ListVoiceConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnectors" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_list

        out["voice_connectors"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_list.deserialize_json(
                data["VoiceConnectors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
