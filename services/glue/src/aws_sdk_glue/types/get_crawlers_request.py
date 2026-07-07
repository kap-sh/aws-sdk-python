"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.token


class GetCrawlersRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The number of crawlers to return on each call.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlersRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlersRequest:
    out: GetCrawlersRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
