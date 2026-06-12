"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListReviewTemplatesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.next_token


class ListReviewTemplatesInput(TypedDict):
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["aws_sdk_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReviewTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReviewTemplatesInput:
    out: ListReviewTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
