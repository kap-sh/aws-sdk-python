"""Generated from Smithy shape ``com.amazonaws.efs#DescribeAccountPreferencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.max_results
    import aws_sdk_efs.types.token


class DescribeAccountPreferencesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p>(Optional) You can use <code>NextToken</code> in a subsequent request to fetch the next page of Amazon Web Services account preferences if the response payload was paginated.</p>"""
    max_results: NotRequired["aws_sdk_efs.types.max_results.MaxResults"]
    """<p>(Optional) When retrieving account preferences, you can optionally specify the <code>MaxItems</code> parameter to limit the number of objects returned in a response. The default value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountPreferencesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeAccountPreferencesRequest:
    out: DescribeAccountPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
