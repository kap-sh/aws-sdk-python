"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListDatasetsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p> The token for the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of datasets to return per page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
