"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListResponsePlansInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.max_results
    import aws_sdk_ssm_incidents.types.next_token


class ListResponsePlansInput(TypedDict):
    max_results: NotRequired["aws_sdk_ssm_incidents.types.max_results.MaxResults"]
    """<p>The maximum number of response plans per page.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResponsePlansInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResponsePlansInput:
    out: ListResponsePlansInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
