"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListTrafficPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.page_size
    import aws_sdk_mailmanager.types.pagination_token


class ListTrafficPoliciesRequest(TypedDict):
    page_size: NotRequired["aws_sdk_mailmanager.types.page_size.PageSize"]
    """<p>The maximum number of traffic policy resources that are returned per call. You can use NextToken to obtain further traffic policies.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTrafficPoliciesRequest) -> dict:
    out: dict = {}
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTrafficPoliciesRequest:
    out: ListTrafficPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
