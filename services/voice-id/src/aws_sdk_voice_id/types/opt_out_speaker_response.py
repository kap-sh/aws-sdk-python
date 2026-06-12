"""Generated from Smithy shape ``com.amazonaws.voiceid#OptOutSpeakerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.speaker


class OptOutSpeakerResponse(TypedDict):
    speaker: NotRequired["aws_sdk_voice_id.types.speaker.Speaker"]
    """<p>Details about the opted-out speaker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptOutSpeakerResponse) -> dict:
    out: dict = {}
    if "speaker" in value:
        import aws_sdk_voice_id.types.speaker

        out["Speaker"] = aws_sdk_voice_id.types.speaker.serialize_aws_json_1_0(
            value["speaker"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OptOutSpeakerResponse:
    out: OptOutSpeakerResponse = {}  # type: ignore[typeddict-item]
    if "Speaker" in data:
        import aws_sdk_voice_id.types.speaker

        out["speaker"] = aws_sdk_voice_id.types.speaker.deserialize_aws_json_1_0(
            data["Speaker"]
        )
    return out
