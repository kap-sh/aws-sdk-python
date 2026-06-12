"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisIssueDetected``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_items_with_content


class RealTimeContactAnalysisIssueDetected(TypedDict):
    transcript_items: "aws_sdk_connect.types.real_time_contact_analysis_transcript_items_with_content.RealTimeContactAnalysisTranscriptItemsWithContent"
    """<p>List of the transcript items (segments) that are associated with a given issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisIssueDetected) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.real_time_contact_analysis_transcript_items_with_content

    out["TranscriptItems"] = (
        aws_sdk_connect.types.real_time_contact_analysis_transcript_items_with_content.serialize_json(
            value["transcript_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisIssueDetected:
    out: RealTimeContactAnalysisIssueDetected = {}  # type: ignore[typeddict-item]
    if "TranscriptItems" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_transcript_items_with_content

        out["transcript_items"] = (
            aws_sdk_connect.types.real_time_contact_analysis_transcript_items_with_content.deserialize_json(
                data["TranscriptItems"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisIssueDetected.transcript_items required"
        )
    return out
