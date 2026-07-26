"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentTranscript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.display_name
    import capo_connect.types.participant_id
    import capo_connect.types.participant_role
    import capo_connect.types.real_time_contact_analysis_content_type
    import capo_connect.types.real_time_contact_analysis_id256
    import capo_connect.types.real_time_contact_analysis_sentiment_label
    import capo_connect.types.real_time_contact_analysis_time_data
    import capo_connect.types.real_time_contact_analysis_transcript_content
    import capo_connect.types.real_time_contact_analysis_transcript_item_redaction


class RealTimeContactAnalysisSegmentTranscript(TypedDict, closed=True):
    id: "capo_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>The identifier of the transcript.</p>"""
    participant_id: "capo_connect.types.participant_id.ParticipantId"
    """<p>The identifier of the participant.</p>"""
    participant_role: "capo_connect.types.participant_role.ParticipantRole"
    """<p>The role of the participant. For example, is it a customer, agent, or system.</p>"""
    display_name: NotRequired["capo_connect.types.display_name.DisplayName"]
    """<p>The display name of the participant.</p>"""
    content: "capo_connect.types.real_time_contact_analysis_transcript_content.RealTimeContactAnalysisTranscriptContent"
    """<p>The content of the transcript. Can be redacted.</p>"""
    content_type: NotRequired[
        "capo_connect.types.real_time_contact_analysis_content_type.RealTimeContactAnalysisContentType"
    ]
    """<p>The type of content of the item. For example, <code>text/plain</code>.</p>"""
    time: "capo_connect.types.real_time_contact_analysis_time_data.RealTimeContactAnalysisTimeData"
    """<p>Field describing the time of the event. It can have different representations of time.</p>"""
    redaction: NotRequired[
        "capo_connect.types.real_time_contact_analysis_transcript_item_redaction.RealTimeContactAnalysisTranscriptItemRedaction"
    ]
    """<p>Object describing redaction that was applied to the transcript. If transcript has the field it means part of the transcript was redacted.</p>"""
    sentiment: NotRequired[
        "capo_connect.types.real_time_contact_analysis_sentiment_label.RealTimeContactAnalysisSentimentLabel"
    ]
    """<p>The sentiment detected for this piece of transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentTranscript) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["ParticipantId"] = value["participant_id"]
    import capo_connect.types.participant_role

    out["ParticipantRole"] = capo_connect.types.participant_role.serialize_json(
        value["participant_role"]
    )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    out["Content"] = value["content"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    import capo_connect.types.real_time_contact_analysis_time_data

    out["Time"] = (
        capo_connect.types.real_time_contact_analysis_time_data.serialize_json(
            value["time"]
        )
    )
    if "redaction" in value:
        import capo_connect.types.real_time_contact_analysis_transcript_item_redaction

        out["Redaction"] = (
            capo_connect.types.real_time_contact_analysis_transcript_item_redaction.serialize_json(
                value["redaction"]
            )
        )
    if "sentiment" in value:
        import capo_connect.types.real_time_contact_analysis_sentiment_label

        out["Sentiment"] = (
            capo_connect.types.real_time_contact_analysis_sentiment_label.serialize_json(
                value["sentiment"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentTranscript:
    out: RealTimeContactAnalysisSegmentTranscript = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentTranscript.id required"
        )
    if "ParticipantId" in data:
        out["participant_id"] = data["ParticipantId"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentTranscript.participant_id required"
        )
    if "ParticipantRole" in data:
        import capo_connect.types.participant_role

        out["participant_role"] = capo_connect.types.participant_role.deserialize_json(
            data["ParticipantRole"]
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentTranscript.participant_role required"
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentTranscript.content required"
        )
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "Time" in data:
        import capo_connect.types.real_time_contact_analysis_time_data

        out["time"] = (
            capo_connect.types.real_time_contact_analysis_time_data.deserialize_json(
                data["Time"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentTranscript.time required"
        )
    if "Redaction" in data:
        import capo_connect.types.real_time_contact_analysis_transcript_item_redaction

        out["redaction"] = (
            capo_connect.types.real_time_contact_analysis_transcript_item_redaction.deserialize_json(
                data["Redaction"]
            )
        )
    if "Sentiment" in data:
        import capo_connect.types.real_time_contact_analysis_sentiment_label

        out["sentiment"] = (
            capo_connect.types.real_time_contact_analysis_sentiment_label.deserialize_json(
                data["Sentiment"]
            )
        )
    return out
