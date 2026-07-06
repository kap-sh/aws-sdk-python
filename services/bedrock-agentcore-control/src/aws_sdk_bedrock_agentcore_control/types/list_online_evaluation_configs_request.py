"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListOnlineEvaluationConfigsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListOnlineEvaluationConfigsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p> The pagination token from a previous request to retrieve the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of online evaluation configurations to return in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOnlineEvaluationConfigsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOnlineEvaluationConfigsRequest:
    out: ListOnlineEvaluationConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
