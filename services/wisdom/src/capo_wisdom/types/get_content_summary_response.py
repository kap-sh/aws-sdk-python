"""Generated from Smithy shape ``com.amazonaws.wisdom#GetContentSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.content_summary


class GetContentSummaryResponse(TypedDict, closed=True):
    content_summary: NotRequired["capo_wisdom.types.content_summary.ContentSummary"]
    """<p>The content summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentSummaryResponse) -> dict:
    out: dict = {}
    if "content_summary" in value:
        import capo_wisdom.types.content_summary

        out["contentSummary"] = capo_wisdom.types.content_summary.serialize_json(
            value["content_summary"]
        )
    return out


def deserialize_json(data: dict) -> GetContentSummaryResponse:
    out: GetContentSummaryResponse = {}  # type: ignore[typeddict-item]
    if "contentSummary" in data:
        import capo_wisdom.types.content_summary

        out["content_summary"] = capo_wisdom.types.content_summary.deserialize_json(
            data["contentSummary"]
        )
    return out
