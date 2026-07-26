"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListStreamingAccessForServicesInput``."""

from typing_extensions import NotRequired, TypedDict


class ListStreamingAccessForServicesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of streaming access entries to return in the response. If there are more results available, the response includes a NextToken value that you can use in a subsequent call to get the next set of results. The value must be between 1 and 50. If you don't specify a value, the default is 50.</p>"""
    next_token: NotRequired["str"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamingAccessForServicesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamingAccessForServicesInput:
    out: ListStreamingAccessForServicesInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
