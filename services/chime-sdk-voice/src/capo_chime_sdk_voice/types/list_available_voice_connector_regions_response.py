"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListAvailableVoiceConnectorRegionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector_aws_region_list


class ListAvailableVoiceConnectorRegionsResponse(TypedDict, closed=True):
    voice_connector_regions: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_aws_region_list.VoiceConnectorAwsRegionList"
    ]
    """<p>The list of AWS Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAvailableVoiceConnectorRegionsResponse) -> dict:
    out: dict = {}
    if "voice_connector_regions" in value:
        import capo_chime_sdk_voice.types.voice_connector_aws_region_list

        out["VoiceConnectorRegions"] = (
            capo_chime_sdk_voice.types.voice_connector_aws_region_list.serialize_json(
                value["voice_connector_regions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAvailableVoiceConnectorRegionsResponse:
    out: ListAvailableVoiceConnectorRegionsResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorRegions" in data:
        import capo_chime_sdk_voice.types.voice_connector_aws_region_list

        out["voice_connector_regions"] = (
            capo_chime_sdk_voice.types.voice_connector_aws_region_list.deserialize_json(
                data["VoiceConnectorRegions"]
            )
        )
    return out
