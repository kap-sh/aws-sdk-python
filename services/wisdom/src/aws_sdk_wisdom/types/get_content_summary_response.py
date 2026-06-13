"""Generated from Smithy shape ``com.amazonaws.wisdom#GetContentSummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.content_summary


class GetContentSummaryResponse(TypedDict):
    content_summary: NotRequired["aws_sdk_wisdom.types.content_summary.ContentSummary"]
    """<p>The content summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentSummaryResponse) -> dict:
    out: dict = {}
    if "content_summary" in value:
        import aws_sdk_wisdom.types.content_summary

        out["contentSummary"] = aws_sdk_wisdom.types.content_summary.serialize_json(
            value["content_summary"]
        )
    return out


def deserialize_json(data: dict) -> GetContentSummaryResponse:
    out: GetContentSummaryResponse = {}  # type: ignore[typeddict-item]
    if "contentSummary" in data:
        import aws_sdk_wisdom.types.content_summary

        out["content_summary"] = aws_sdk_wisdom.types.content_summary.deserialize_json(
            data["contentSummary"]
        )
    return out
