"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPartnerAppsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token


class ListPartnerAppsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>This parameter defines the maximum number of results that can be returned in a single response. The <code>MaxResults</code> parameter is an upper bound, not a target. If there are more results available than the value specified, a <code>NextToken</code> is provided in the response. The <code>NextToken</code> indicates that the user should get the next set of results by providing this token as a part of a subsequent call. The default value for <code>MaxResults</code> is 10.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerAppsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerAppsRequest:
    out: ListPartnerAppsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
