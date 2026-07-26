"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisPointOfInterest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets


class RealTimeContactAnalysisPointOfInterest(TypedDict, closed=True):
    transcript_items: NotRequired[
        "capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets.RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets"
    ]
    """<p>List of the transcript items (segments) that are associated with a given point of interest. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisPointOfInterest) -> dict:
    out: dict = {}
    if "transcript_items" in value:
        import capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets

        out["TranscriptItems"] = (
            capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets.serialize_json(
                value["transcript_items"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisPointOfInterest:
    out: RealTimeContactAnalysisPointOfInterest = {}  # type: ignore[typeddict-item]
    if "TranscriptItems" in data:
        import capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets

        out["transcript_items"] = (
            capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets.deserialize_json(
                data["TranscriptItems"]
            )
        )
    return out
