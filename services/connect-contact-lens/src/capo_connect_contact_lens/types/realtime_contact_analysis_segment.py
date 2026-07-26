"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#RealtimeContactAnalysisSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.categories
    import capo_connect_contact_lens.types.post_contact_summary
    import capo_connect_contact_lens.types.transcript


class RealtimeContactAnalysisSegment(TypedDict, closed=True):
    transcript: NotRequired["capo_connect_contact_lens.types.transcript.Transcript"]
    """<p>The analyzed transcript.</p>"""
    categories: NotRequired["capo_connect_contact_lens.types.categories.Categories"]
    """<p>The matched category rules.</p>"""
    post_contact_summary: NotRequired[
        "capo_connect_contact_lens.types.post_contact_summary.PostContactSummary"
    ]
    """<p>Information about the post-contact summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealtimeContactAnalysisSegment) -> dict:
    out: dict = {}
    if "transcript" in value:
        import capo_connect_contact_lens.types.transcript

        out["Transcript"] = capo_connect_contact_lens.types.transcript.serialize_json(
            value["transcript"]
        )
    if "categories" in value:
        import capo_connect_contact_lens.types.categories

        out["Categories"] = capo_connect_contact_lens.types.categories.serialize_json(
            value["categories"]
        )
    if "post_contact_summary" in value:
        import capo_connect_contact_lens.types.post_contact_summary

        out["PostContactSummary"] = (
            capo_connect_contact_lens.types.post_contact_summary.serialize_json(
                value["post_contact_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealtimeContactAnalysisSegment:
    out: RealtimeContactAnalysisSegment = {}  # type: ignore[typeddict-item]
    if "Transcript" in data:
        import capo_connect_contact_lens.types.transcript

        out["transcript"] = capo_connect_contact_lens.types.transcript.deserialize_json(
            data["Transcript"]
        )
    if "Categories" in data:
        import capo_connect_contact_lens.types.categories

        out["categories"] = capo_connect_contact_lens.types.categories.deserialize_json(
            data["Categories"]
        )
    if "PostContactSummary" in data:
        import capo_connect_contact_lens.types.post_contact_summary

        out["post_contact_summary"] = (
            capo_connect_contact_lens.types.post_contact_summary.deserialize_json(
                data["PostContactSummary"]
            )
        )
    return out
