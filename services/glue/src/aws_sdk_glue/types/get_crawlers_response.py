"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_list
    import aws_sdk_glue.types.token


class GetCrawlersResponse(TypedDict):
    crawlers: NotRequired["aws_sdk_glue.types.crawler_list.CrawlerList"]
    """<p>A list of crawler metadata.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if the returned list has not reached the end of those defined in this customer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlersResponse) -> dict:
    out: dict = {}
    if "crawlers" in value:
        import aws_sdk_glue.types.crawler_list

        out["Crawlers"] = aws_sdk_glue.types.crawler_list.serialize_aws_json_1_1(
            value["crawlers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlersResponse:
    out: GetCrawlersResponse = {}  # type: ignore[typeddict-item]
    if "Crawlers" in data:
        import aws_sdk_glue.types.crawler_list

        out["crawlers"] = aws_sdk_glue.types.crawler_list.deserialize_aws_json_1_1(
            data["Crawlers"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
