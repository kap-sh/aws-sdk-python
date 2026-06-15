"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListEvaluatorsRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListEvaluatorsRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p> The pagination token from a previous request to retrieve the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of evaluators to return in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluatorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEvaluatorsRequest:
    out: ListEvaluatorsRequest = {}  # type: ignore[typeddict-item]
    return out
