"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeEntitlementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.integer
    import capo_appstream.types.name
    import capo_appstream.types.string


class DescribeEntitlementsRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    stack_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the stack with which the entitlement is associated.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitlementsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitlementsRequest:
    out: DescribeEntitlementsRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
