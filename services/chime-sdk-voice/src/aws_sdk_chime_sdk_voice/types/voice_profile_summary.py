"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.arn
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class VoiceProfileSummary(TypedDict, closed=True):
    voice_profile_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The ID of the voice profile in a voice profile summary.</p>"""
    voice_profile_arn: NotRequired["aws_sdk_chime_sdk_voice.types.arn.Arn"]
    """<p>The ARN of the voice profile in a voice profile summary.</p>"""
    voice_profile_domain_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The ID of the voice profile domain in a voice profile summary.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice profile summary was created.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice profile summary was last updated.</p>"""
    expiration_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>Extends the life of the voice profile. You can use <code>UpdateVoiceProfile</code> to refresh an existing voice profile's voice print and extend the life of the summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceProfileSummary) -> dict:
    out: dict = {}
    if "voice_profile_id" in value:
        out["VoiceProfileId"] = value["voice_profile_id"]
    if "voice_profile_arn" in value:
        out["VoiceProfileArn"] = value["voice_profile_arn"]
    if "voice_profile_domain_id" in value:
        out["VoiceProfileDomainId"] = value["voice_profile_domain_id"]
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "expiration_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["ExpirationTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["expiration_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceProfileSummary:
    out: VoiceProfileSummary = {}  # type: ignore[typeddict-item]
    if "VoiceProfileId" in data:
        out["voice_profile_id"] = data["VoiceProfileId"]
    if "VoiceProfileArn" in data:
        out["voice_profile_arn"] = data["VoiceProfileArn"]
    if "VoiceProfileDomainId" in data:
        out["voice_profile_domain_id"] = data["VoiceProfileDomainId"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "ExpirationTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["expiration_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["ExpirationTimestamp"]
            )
        )
    return out
