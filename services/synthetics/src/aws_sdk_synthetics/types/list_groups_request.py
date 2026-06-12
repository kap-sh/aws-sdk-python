"""Generated from Smithy shape ``com.amazonaws.synthetics#ListGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.max_group_results
    import aws_sdk_synthetics.types.pagination_token


class ListGroupsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_synthetics.types.pagination_token.PaginationToken"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_synthetics.types.max_group_results.MaxGroupResults"
    ]
    """<p>Specify this parameter to limit how many groups are returned each time you use the <code>ListGroups</code> operation. If you omit this parameter, the default of 20 is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListGroupsRequest:
    out: ListGroupsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
