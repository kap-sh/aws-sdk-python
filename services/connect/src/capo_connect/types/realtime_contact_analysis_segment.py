"""Generated from Smithy shape ``com.amazonaws.connect#RealtimeContactAnalysisSegment``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_segment_attachments
    import capo_connect.types.real_time_contact_analysis_segment_categories
    import capo_connect.types.real_time_contact_analysis_segment_event
    import capo_connect.types.real_time_contact_analysis_segment_issues
    import capo_connect.types.real_time_contact_analysis_segment_post_contact_summary
    import capo_connect.types.real_time_contact_analysis_segment_transcript


class _RealtimeContactAnalysisSegment_Transcript(TypedDict, closed=True):
    Transcript: "capo_connect.types.real_time_contact_analysis_segment_transcript.RealTimeContactAnalysisSegmentTranscript"


class _RealtimeContactAnalysisSegment_Categories(TypedDict, closed=True):
    Categories: "capo_connect.types.real_time_contact_analysis_segment_categories.RealTimeContactAnalysisSegmentCategories"


class _RealtimeContactAnalysisSegment_Issues(TypedDict, closed=True):
    Issues: "capo_connect.types.real_time_contact_analysis_segment_issues.RealTimeContactAnalysisSegmentIssues"


class _RealtimeContactAnalysisSegment_Event(TypedDict, closed=True):
    Event: "capo_connect.types.real_time_contact_analysis_segment_event.RealTimeContactAnalysisSegmentEvent"


class _RealtimeContactAnalysisSegment_Attachments(TypedDict, closed=True):
    Attachments: "capo_connect.types.real_time_contact_analysis_segment_attachments.RealTimeContactAnalysisSegmentAttachments"


class _RealtimeContactAnalysisSegment_PostContactSummary(TypedDict, closed=True):
    PostContactSummary: "capo_connect.types.real_time_contact_analysis_segment_post_contact_summary.RealTimeContactAnalysisSegmentPostContactSummary"


RealtimeContactAnalysisSegment: TypeAlias = (
    _RealtimeContactAnalysisSegment_Transcript
    | _RealtimeContactAnalysisSegment_Categories
    | _RealtimeContactAnalysisSegment_Issues
    | _RealtimeContactAnalysisSegment_Event
    | _RealtimeContactAnalysisSegment_Attachments
    | _RealtimeContactAnalysisSegment_PostContactSummary
)


# --- restJson1 ser/de ---
def serialize_json(value: RealtimeContactAnalysisSegment) -> dict:
    if "Transcript" in value:
        import capo_connect.types.real_time_contact_analysis_segment_transcript

        return {
            "Transcript": capo_connect.types.real_time_contact_analysis_segment_transcript.serialize_json(
                value["Transcript"]
            )
        }
    elif "Categories" in value:
        import capo_connect.types.real_time_contact_analysis_segment_categories

        return {
            "Categories": capo_connect.types.real_time_contact_analysis_segment_categories.serialize_json(
                value["Categories"]
            )
        }
    elif "Issues" in value:
        import capo_connect.types.real_time_contact_analysis_segment_issues

        return {
            "Issues": capo_connect.types.real_time_contact_analysis_segment_issues.serialize_json(
                value["Issues"]
            )
        }
    elif "Event" in value:
        import capo_connect.types.real_time_contact_analysis_segment_event

        return {
            "Event": capo_connect.types.real_time_contact_analysis_segment_event.serialize_json(
                value["Event"]
            )
        }
    elif "Attachments" in value:
        import capo_connect.types.real_time_contact_analysis_segment_attachments

        return {
            "Attachments": capo_connect.types.real_time_contact_analysis_segment_attachments.serialize_json(
                value["Attachments"]
            )
        }
    elif "PostContactSummary" in value:
        import capo_connect.types.real_time_contact_analysis_segment_post_contact_summary

        return {
            "PostContactSummary": capo_connect.types.real_time_contact_analysis_segment_post_contact_summary.serialize_json(
                value["PostContactSummary"]
            )
        }
    else:
        raise SerializationError("RealtimeContactAnalysisSegment: no variant present")


def deserialize_json(data: dict) -> RealtimeContactAnalysisSegment:
    if "Transcript" in data:
        import capo_connect.types.real_time_contact_analysis_segment_transcript

        return {
            "Transcript": capo_connect.types.real_time_contact_analysis_segment_transcript.deserialize_json(
                data["Transcript"]
            )
        }
    elif "Categories" in data:
        import capo_connect.types.real_time_contact_analysis_segment_categories

        return {
            "Categories": capo_connect.types.real_time_contact_analysis_segment_categories.deserialize_json(
                data["Categories"]
            )
        }
    elif "Issues" in data:
        import capo_connect.types.real_time_contact_analysis_segment_issues

        return {
            "Issues": capo_connect.types.real_time_contact_analysis_segment_issues.deserialize_json(
                data["Issues"]
            )
        }
    elif "Event" in data:
        import capo_connect.types.real_time_contact_analysis_segment_event

        return {
            "Event": capo_connect.types.real_time_contact_analysis_segment_event.deserialize_json(
                data["Event"]
            )
        }
    elif "Attachments" in data:
        import capo_connect.types.real_time_contact_analysis_segment_attachments

        return {
            "Attachments": capo_connect.types.real_time_contact_analysis_segment_attachments.deserialize_json(
                data["Attachments"]
            )
        }
    elif "PostContactSummary" in data:
        import capo_connect.types.real_time_contact_analysis_segment_post_contact_summary

        return {
            "PostContactSummary": capo_connect.types.real_time_contact_analysis_segment_post_contact_summary.deserialize_json(
                data["PostContactSummary"]
            )
        }
    else:
        raise DeserializationError(
            "RealtimeContactAnalysisSegment: no recognized variant key"
        )
