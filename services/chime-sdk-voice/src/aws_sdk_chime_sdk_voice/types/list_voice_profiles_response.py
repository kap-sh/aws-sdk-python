"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.voice_profile_summary_list


class ListVoiceProfilesResponse(TypedDict):
    voice_profiles: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_profile_summary_list.VoiceProfileSummaryList"
    ]
    """<p>The list of voice profiles.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The token used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceProfilesResponse) -> dict:
    out: dict = {}
    if "voice_profiles" in value:
        import aws_sdk_chime_sdk_voice.types.voice_profile_summary_list

        out["VoiceProfiles"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile_summary_list.serialize_json(
                value["voice_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVoiceProfilesResponse:
    out: ListVoiceProfilesResponse = {}  # type: ignore[typeddict-item]
    if "VoiceProfiles" in data:
        import aws_sdk_chime_sdk_voice.types.voice_profile_summary_list

        out["voice_profiles"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile_summary_list.deserialize_json(
                data["VoiceProfiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
