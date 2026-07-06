"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token


class ListDomainsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>This parameter defines the maximum number of results that can be return in a single response. The <code>MaxResults</code> parameter is an upper bound, not a target. If there are more results available than the value specified, a <code>NextToken</code> is provided in the response. The <code>NextToken</code> indicates that the user should get the next set of results by providing this token as a part of a subsequent call. The default value for <code>MaxResults</code> is 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDomainsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
