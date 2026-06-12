"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#RealtimeContactAnalysisSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.categories
    import aws_sdk_connect_contact_lens.types.post_contact_summary
    import aws_sdk_connect_contact_lens.types.transcript


class RealtimeContactAnalysisSegment(TypedDict):
    transcript: NotRequired["aws_sdk_connect_contact_lens.types.transcript.Transcript"]
    """<p>The analyzed transcript.</p>"""
    categories: NotRequired["aws_sdk_connect_contact_lens.types.categories.Categories"]
    """<p>The matched category rules.</p>"""
    post_contact_summary: NotRequired[
        "aws_sdk_connect_contact_lens.types.post_contact_summary.PostContactSummary"
    ]
    """<p>Information about the post-contact summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealtimeContactAnalysisSegment) -> dict:
    out: dict = {}
    if "transcript" in value:
        import aws_sdk_connect_contact_lens.types.transcript

        out["Transcript"] = (
            aws_sdk_connect_contact_lens.types.transcript.serialize_json(
                value["transcript"]
            )
        )
    if "categories" in value:
        import aws_sdk_connect_contact_lens.types.categories

        out["Categories"] = (
            aws_sdk_connect_contact_lens.types.categories.serialize_json(
                value["categories"]
            )
        )
    if "post_contact_summary" in value:
        import aws_sdk_connect_contact_lens.types.post_contact_summary

        out["PostContactSummary"] = (
            aws_sdk_connect_contact_lens.types.post_contact_summary.serialize_json(
                value["post_contact_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealtimeContactAnalysisSegment:
    out: RealtimeContactAnalysisSegment = {}  # type: ignore[typeddict-item]
    if "Transcript" in data:
        import aws_sdk_connect_contact_lens.types.transcript

        out["transcript"] = (
            aws_sdk_connect_contact_lens.types.transcript.deserialize_json(
                data["Transcript"]
            )
        )
    if "Categories" in data:
        import aws_sdk_connect_contact_lens.types.categories

        out["categories"] = (
            aws_sdk_connect_contact_lens.types.categories.deserialize_json(
                data["Categories"]
            )
        )
    if "PostContactSummary" in data:
        import aws_sdk_connect_contact_lens.types.post_contact_summary

        out["post_contact_summary"] = (
            aws_sdk_connect_contact_lens.types.post_contact_summary.deserialize_json(
                data["PostContactSummary"]
            )
        )
    return out
