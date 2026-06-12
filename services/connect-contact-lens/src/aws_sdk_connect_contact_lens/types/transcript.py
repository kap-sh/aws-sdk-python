"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#Transcript``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.issues_detected
    import aws_sdk_connect_contact_lens.types.offset_millis
    import aws_sdk_connect_contact_lens.types.participant_id
    import aws_sdk_connect_contact_lens.types.participant_role
    import aws_sdk_connect_contact_lens.types.sentiment_value
    import aws_sdk_connect_contact_lens.types.transcript_content
    import aws_sdk_connect_contact_lens.types.transcript_id


class Transcript(TypedDict):
    id: NotRequired["aws_sdk_connect_contact_lens.types.transcript_id.TranscriptId"]
    """<p>The identifier of the transcript.</p>"""
    participant_id: NotRequired[
        "aws_sdk_connect_contact_lens.types.participant_id.ParticipantId"
    ]
    """<p>The identifier of the participant. Valid values are CUSTOMER or AGENT.</p>"""
    participant_role: NotRequired[
        "aws_sdk_connect_contact_lens.types.participant_role.ParticipantRole"
    ]
    """<p>The role of participant. For example, is it a customer, agent, or system.</p>"""
    content: NotRequired[
        "aws_sdk_connect_contact_lens.types.transcript_content.TranscriptContent"
    ]
    """<p>The content of the transcript.</p>"""
    begin_offset_millis: NotRequired[
        "aws_sdk_connect_contact_lens.types.offset_millis.OffsetMillis"
    ]
    """<p>The beginning offset in the contact for this transcript.</p>"""
    end_offset_millis: NotRequired[
        "aws_sdk_connect_contact_lens.types.offset_millis.OffsetMillis"
    ]
    """<p>The end offset in the contact for this transcript.</p>"""
    sentiment: NotRequired[
        "aws_sdk_connect_contact_lens.types.sentiment_value.SentimentValue"
    ]
    """<p>The sentiment detected for this piece of transcript.</p>"""
    issues_detected: NotRequired[
        "aws_sdk_connect_contact_lens.types.issues_detected.IssuesDetected"
    ]
    """<p>List of positions where issues were detected on the transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transcript) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "participant_role" in value:
        out["ParticipantRole"] = value["participant_role"]
    if "content" in value:
        out["Content"] = value["content"]
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    if "sentiment" in value:
        import aws_sdk_connect_contact_lens.types.sentiment_value

        out["Sentiment"] = (
            aws_sdk_connect_contact_lens.types.sentiment_value.serialize_json(
                value["sentiment"]
            )
        )
    if "issues_detected" in value:
        import aws_sdk_connect_contact_lens.types.issues_detected

        out["IssuesDetected"] = (
            aws_sdk_connect_contact_lens.types.issues_detected.serialize_json(
                value["issues_detected"]
            )
        )
    return out


def deserialize_json(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ParticipantId" in data:
        out["participant_id"] = data["ParticipantId"]
    if "ParticipantRole" in data:
        out["participant_role"] = data["ParticipantRole"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    if "Sentiment" in data:
        import aws_sdk_connect_contact_lens.types.sentiment_value

        out["sentiment"] = (
            aws_sdk_connect_contact_lens.types.sentiment_value.deserialize_json(
                data["Sentiment"]
            )
        )
    if "IssuesDetected" in data:
        import aws_sdk_connect_contact_lens.types.issues_detected

        out["issues_detected"] = (
            aws_sdk_connect_contact_lens.types.issues_detected.deserialize_json(
                data["IssuesDetected"]
            )
        )
    return out
