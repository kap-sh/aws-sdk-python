"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeSpeakerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.speaker_id


class DescribeSpeakerRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the speaker.</p>"""
    speaker_id: "capo_voice_id.types.speaker_id.SpeakerId"
    """<p>The identifier of the speaker you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeSpeakerRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["SpeakerId"] = value["speaker_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeSpeakerRequest:
    out: DescribeSpeakerRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("DescribeSpeakerRequest.domain_id required")
    if "SpeakerId" in data:
        out["speaker_id"] = data["SpeakerId"]
    else:
        raise DeserializationError("DescribeSpeakerRequest.speaker_id required")
    return out
