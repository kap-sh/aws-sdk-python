"""Generated from Smithy shape ``com.amazonaws.appstream#ListEntitledApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.string


class ListEntitledApplicationsRequest(TypedDict):
    stack_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the stack with which the entitlement is associated.</p>"""
    entitlement_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the entitlement.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitledApplicationsRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "entitlement_name" in value:
        out["EntitlementName"] = value["entitlement_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitledApplicationsRequest:
    out: ListEntitledApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "EntitlementName" in data:
        out["entitlement_name"] = data["EntitlementName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
