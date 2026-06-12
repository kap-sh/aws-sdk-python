"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#UtteranceEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.boolean
    import aws_sdk_transcribe_streaming.types.call_analytics_entity_list
    import aws_sdk_transcribe_streaming.types.call_analytics_item_list
    import aws_sdk_transcribe_streaming.types.call_analytics_language_code
    import aws_sdk_transcribe_streaming.types.call_analytics_language_identification
    import aws_sdk_transcribe_streaming.types.issues_detected
    import aws_sdk_transcribe_streaming.types.long
    import aws_sdk_transcribe_streaming.types.participant_role
    import aws_sdk_transcribe_streaming.types.sentiment
    import aws_sdk_transcribe_streaming.types.string


class UtteranceEvent(TypedDict):
    utterance_id: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The unique identifier that is associated with the specified <code>UtteranceEvent</code>.</p>"""
    is_partial: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Indicates whether the segment in the <code>UtteranceEvent</code> is complete (<code>FALSE</code>) or partial (<code>TRUE</code>).</p>"""
    participant_role: NotRequired[
        "aws_sdk_transcribe_streaming.types.participant_role.ParticipantRole"
    ]
    """<p>Provides the role of the speaker for each audio channel, either <code>CUSTOMER</code> or <code>AGENT</code>.</p>"""
    begin_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the <code>UtteranceEvent</code>.</p>"""
    end_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the <code>UtteranceEvent</code>.</p>"""
    transcript: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>Contains transcribed text.</p>"""
    items: NotRequired[
        "aws_sdk_transcribe_streaming.types.call_analytics_item_list.CallAnalyticsItemList"
    ]
    """<p>Contains words, phrases, or punctuation marks that are associated with the specified <code>UtteranceEvent</code>.</p>"""
    entities: NotRequired[
        "aws_sdk_transcribe_streaming.types.call_analytics_entity_list.CallAnalyticsEntityList"
    ]
    """<p>Contains entities identified as personally identifiable information (PII) in your transcription output.</p>"""
    sentiment: NotRequired["aws_sdk_transcribe_streaming.types.sentiment.Sentiment"]
    """<p>Provides the sentiment that was detected in the specified segment.</p>"""
    issues_detected: NotRequired[
        "aws_sdk_transcribe_streaming.types.issues_detected.IssuesDetected"
    ]
    """<p>Provides the issue that was detected in the specified segment.</p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>The language code that represents the language spoken in your audio stream.</p>"""
    language_identification: NotRequired[
        "aws_sdk_transcribe_streaming.types.call_analytics_language_identification.CallAnalyticsLanguageIdentification"
    ]
    """<p>The language code of the dominant language identified in your stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceEvent) -> dict:
    out: dict = {}
    if "utterance_id" in value:
        out["UtteranceId"] = value["utterance_id"]
    out["IsPartial"] = value.get("is_partial", False)
    if "participant_role" in value:
        import aws_sdk_transcribe_streaming.types.participant_role

        out["ParticipantRole"] = (
            aws_sdk_transcribe_streaming.types.participant_role.serialize_json(
                value["participant_role"]
            )
        )
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    if "transcript" in value:
        out["Transcript"] = value["transcript"]
    if "items" in value:
        import aws_sdk_transcribe_streaming.types.call_analytics_item_list

        out["Items"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_item_list.serialize_json(
                value["items"]
            )
        )
    if "entities" in value:
        import aws_sdk_transcribe_streaming.types.call_analytics_entity_list

        out["Entities"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_entity_list.serialize_json(
                value["entities"]
            )
        )
    if "sentiment" in value:
        import aws_sdk_transcribe_streaming.types.sentiment

        out["Sentiment"] = aws_sdk_transcribe_streaming.types.sentiment.serialize_json(
            value["sentiment"]
        )
    if "issues_detected" in value:
        import aws_sdk_transcribe_streaming.types.issues_detected

        out["IssuesDetected"] = (
            aws_sdk_transcribe_streaming.types.issues_detected.serialize_json(
                value["issues_detected"]
            )
        )
    if "language_code" in value:
        import aws_sdk_transcribe_streaming.types.call_analytics_language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "language_identification" in value:
        import aws_sdk_transcribe_streaming.types.call_analytics_language_identification

        out["LanguageIdentification"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_language_identification.serialize_json(
                value["language_identification"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceEvent:
    out: UtteranceEvent = {}  # type: ignore[typeddict-item]
    if "UtteranceId" in data:
        out["utterance_id"] = data["UtteranceId"]
    if "IsPartial" in data:
        out["is_partial"] = data["IsPartial"]
    else:
        out["is_partial"] = False
    if "ParticipantRole" in data:
        import aws_sdk_transcribe_streaming.types.participant_role

        out["participant_role"] = (
            aws_sdk_transcribe_streaming.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    if "Transcript" in data:
        out["transcript"] = data["Transcript"]
    if "Items" in data:
        import aws_sdk_transcribe_streaming.types.call_analytics_item_list

        out["items"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_item_list.deserialize_json(
                data["Items"]
            )
        )
    if "Entities" in data:
        import aws_sdk_transcribe_streaming.types.call_analytics_entity_list

        out["entities"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_entity_list.deserialize_json(
                data["Entities"]
            )
        )
    if "Sentiment" in data:
        import aws_sdk_transcribe_streaming.types.sentiment

        out["sentiment"] = (
            aws_sdk_transcribe_streaming.types.sentiment.deserialize_json(
                data["Sentiment"]
            )
        )
    if "IssuesDetected" in data:
        import aws_sdk_transcribe_streaming.types.issues_detected

        out["issues_detected"] = (
            aws_sdk_transcribe_streaming.types.issues_detected.deserialize_json(
                data["IssuesDetected"]
            )
        )
    if "LanguageCode" in data:
        import aws_sdk_transcribe_streaming.types.call_analytics_language_code

        out["language_code"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if "LanguageIdentification" in data:
        import aws_sdk_transcribe_streaming.types.call_analytics_language_identification

        out["language_identification"] = (
            aws_sdk_transcribe_streaming.types.call_analytics_language_identification.deserialize_json(
                data["LanguageIdentification"]
            )
        )
    return out
