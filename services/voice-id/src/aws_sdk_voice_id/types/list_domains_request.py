"""Generated from Smithy shape ``com.amazonaws.voiceid#ListDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.max_results_for_list_domain_fe
    import aws_sdk_voice_id.types.next_token


class ListDomainsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
    ]
    """<p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>"""
    next_token: NotRequired["aws_sdk_voice_id.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDomainsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
