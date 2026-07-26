"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token


class ListPoliciesRequest(TypedDict, closed=True):
    max_results: "capo_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPoliciesRequest:
    out: ListPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
