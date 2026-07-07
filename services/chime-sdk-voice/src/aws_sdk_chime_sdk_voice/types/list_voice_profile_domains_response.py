"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceProfileDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.voice_profile_domain_summary_list


class ListVoiceProfileDomainsResponse(TypedDict, closed=True):
    voice_profile_domains: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_profile_domain_summary_list.VoiceProfileDomainSummaryList"
    ]
    """<p>The list of voice profile domains.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceProfileDomainsResponse) -> dict:
    out: dict = {}
    if "voice_profile_domains" in value:
        import aws_sdk_chime_sdk_voice.types.voice_profile_domain_summary_list

        out["VoiceProfileDomains"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile_domain_summary_list.serialize_json(
                value["voice_profile_domains"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVoiceProfileDomainsResponse:
    out: ListVoiceProfileDomainsResponse = {}  # type: ignore[typeddict-item]
    if "VoiceProfileDomains" in data:
        import aws_sdk_chime_sdk_voice.types.voice_profile_domain_summary_list

        out["voice_profile_domains"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile_domain_summary_list.deserialize_json(
                data["VoiceProfileDomains"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
