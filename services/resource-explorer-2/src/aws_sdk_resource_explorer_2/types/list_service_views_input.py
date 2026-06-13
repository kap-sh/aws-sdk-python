"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListServiceViewsInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListServiceViewsInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of service view results to return in a single response. Valid values are between <code>1</code> and <code>50</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from a previous <code>ListServiceViews</code> response. Use this token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceViewsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceViewsInput:
    out: ListServiceViewsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
