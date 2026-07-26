"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListReviewTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token


class ListReviewTemplatesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReviewTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReviewTemplatesInput:
    out: ListReviewTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
