"""Generated from Smithy shape ``com.amazonaws.glue#ListCrawlsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_history_list
    import aws_sdk_glue.types.token


class ListCrawlsResponse(TypedDict):
    crawls: NotRequired["aws_sdk_glue.types.crawler_history_list.CrawlerHistoryList"]
    """<p>A list of <code>CrawlerHistory</code> objects representing the crawl runs that meet your criteria.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrawlsResponse) -> dict:
    out: dict = {}
    if "crawls" in value:
        import aws_sdk_glue.types.crawler_history_list

        out["Crawls"] = aws_sdk_glue.types.crawler_history_list.serialize_aws_json_1_1(
            value["crawls"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrawlsResponse:
    out: ListCrawlsResponse = {}  # type: ignore[typeddict-item]
    if "Crawls" in data:
        import aws_sdk_glue.types.crawler_history_list

        out["crawls"] = (
            aws_sdk_glue.types.crawler_history_list.deserialize_aws_json_1_1(
                data["Crawls"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
