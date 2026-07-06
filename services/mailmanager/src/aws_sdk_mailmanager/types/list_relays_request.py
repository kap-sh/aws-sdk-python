"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListRelaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.pagination_token


class ListRelaysRequest(TypedDict, closed=True):
    page_size: NotRequired["int"]
    """<p>The number of relays to be returned in one request.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelaysRequest) -> dict:
    out: dict = {}
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRelaysRequest:
    out: ListRelaysRequest = {}  # type: ignore[typeddict-item]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
