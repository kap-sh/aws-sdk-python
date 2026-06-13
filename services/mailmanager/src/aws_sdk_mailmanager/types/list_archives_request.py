"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListArchivesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.page_size
    import aws_sdk_mailmanager.types.pagination_token


class ListArchivesRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>"""
    page_size: NotRequired["aws_sdk_mailmanager.types.page_size.PageSize"]
    """<p>The maximum number of archives that are returned per call. You can use NextToken to obtain further pages of archives. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListArchivesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListArchivesRequest:
    out: ListArchivesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    return out
