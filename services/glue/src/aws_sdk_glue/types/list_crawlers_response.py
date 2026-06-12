"""Generated from Smithy shape ``com.amazonaws.glue#ListCrawlersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_name_list
    import aws_sdk_glue.types.token


class ListCrawlersResponse(TypedDict):
    crawler_names: NotRequired["aws_sdk_glue.types.crawler_name_list.CrawlerNameList"]
    """<p>The names of all crawlers in the account, or the crawlers with the specified tags.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if the returned list does not contain the last metric available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrawlersResponse) -> dict:
    out: dict = {}
    if "crawler_names" in value:
        import aws_sdk_glue.types.crawler_name_list

        out["CrawlerNames"] = (
            aws_sdk_glue.types.crawler_name_list.serialize_aws_json_1_1(
                value["crawler_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrawlersResponse:
    out: ListCrawlersResponse = {}  # type: ignore[typeddict-item]
    if "CrawlerNames" in data:
        import aws_sdk_glue.types.crawler_name_list

        out["crawler_names"] = (
            aws_sdk_glue.types.crawler_name_list.deserialize_aws_json_1_1(
                data["CrawlerNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
