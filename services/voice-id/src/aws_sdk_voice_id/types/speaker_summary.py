"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.customer_speaker_id
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.generated_speaker_id
    import aws_sdk_voice_id.types.speaker_status
    import aws_sdk_voice_id.types.timestamp


class SpeakerSummary(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the speaker.</p>"""
    customer_speaker_id: NotRequired[
        "aws_sdk_voice_id.types.customer_speaker_id.CustomerSpeakerId"
    ]
    """<p>The client-provided identifier for the speaker.</p>"""
    generated_speaker_id: NotRequired[
        "aws_sdk_voice_id.types.generated_speaker_id.GeneratedSpeakerId"
    ]
    """<p>The service-generated identifier for the speaker. </p>"""
    status: NotRequired["aws_sdk_voice_id.types.speaker_status.SpeakerStatus"]
    """<p>The current status of the speaker.</p>"""
    created_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp showing the speaker's creation time. </p>"""
    updated_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp showing the speaker's last update.</p>"""
    last_accessed_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp when the speaker was last accessed for enrollment, re-enrollment or a successful authentication. This timestamp is accurate to one hour.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "customer_speaker_id" in value:
        out["CustomerSpeakerId"] = value["customer_speaker_id"]
    if "generated_speaker_id" in value:
        out["GeneratedSpeakerId"] = value["generated_speaker_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "created_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["CreatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["UpdatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "last_accessed_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["LastAccessedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["last_accessed_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SpeakerSummary:
    out: SpeakerSummary = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "CustomerSpeakerId" in data:
        out["customer_speaker_id"] = data["CustomerSpeakerId"]
    if "GeneratedSpeakerId" in data:
        out["generated_speaker_id"] = data["GeneratedSpeakerId"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "CreatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["created_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["updated_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    if "LastAccessedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["last_accessed_at"] = (
            aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
                data["LastAccessedAt"]
            )
        )
    return out
