"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListWorkloadsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.max_workload_results
    import aws_sdk_launch_wizard.types.next_token


class ListWorkloadsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_launch_wizard.types.max_workload_results.MaxWorkloadResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["aws_sdk_launch_wizard.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadsInput:
    out: ListWorkloadsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
