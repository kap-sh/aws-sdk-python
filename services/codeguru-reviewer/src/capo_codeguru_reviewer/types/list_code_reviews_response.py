"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListCodeReviewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.code_review_summaries
    import capo_codeguru_reviewer.types.next_token


class ListCodeReviewsResponse(TypedDict, closed=True):
    code_review_summaries: NotRequired[
        "capo_codeguru_reviewer.types.code_review_summaries.CodeReviewSummaries"
    ]
    """<p>A list of code reviews that meet the criteria of the request.</p>"""
    next_token: NotRequired["capo_codeguru_reviewer.types.next_token.NextToken"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeReviewsResponse) -> dict:
    out: dict = {}
    if "code_review_summaries" in value:
        import capo_codeguru_reviewer.types.code_review_summaries

        out["CodeReviewSummaries"] = (
            capo_codeguru_reviewer.types.code_review_summaries.serialize_json(
                value["code_review_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeReviewsResponse:
    out: ListCodeReviewsResponse = {}  # type: ignore[typeddict-item]
    if "CodeReviewSummaries" in data:
        import capo_codeguru_reviewer.types.code_review_summaries

        out["code_review_summaries"] = (
            capo_codeguru_reviewer.types.code_review_summaries.deserialize_json(
                data["CodeReviewSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
