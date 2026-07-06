"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.max_results
    import aws_sdk_sso_admin.types.token


class ListInstancesRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_sso_admin.types.max_results.MaxResults"]
    """<p>The maximum number of results to display for the instance.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesRequest:
    out: ListInstancesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
