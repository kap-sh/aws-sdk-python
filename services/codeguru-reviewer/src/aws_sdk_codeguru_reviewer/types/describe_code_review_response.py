"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#DescribeCodeReviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.code_review


class DescribeCodeReviewResponse(TypedDict, closed=True):
    code_review: NotRequired["aws_sdk_codeguru_reviewer.types.code_review.CodeReview"]
    """<p>Information about the code review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCodeReviewResponse) -> dict:
    out: dict = {}
    if "code_review" in value:
        import aws_sdk_codeguru_reviewer.types.code_review

        out["CodeReview"] = aws_sdk_codeguru_reviewer.types.code_review.serialize_json(
            value["code_review"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCodeReviewResponse:
    out: DescribeCodeReviewResponse = {}  # type: ignore[typeddict-item]
    if "CodeReview" in data:
        import aws_sdk_codeguru_reviewer.types.code_review

        out["code_review"] = (
            aws_sdk_codeguru_reviewer.types.code_review.deserialize_json(
                data["CodeReview"]
            )
        )
    return out
