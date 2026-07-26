"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlerMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawler_name_list
    import capo_glue.types.page_size
    import capo_glue.types.token


class GetCrawlerMetricsRequest(TypedDict, closed=True):
    crawler_name_list: NotRequired["capo_glue.types.crawler_name_list.CrawlerNameList"]
    """<p>A list of the names of crawlers about which to retrieve metrics.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum size of a list to return.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlerMetricsRequest) -> dict:
    out: dict = {}
    if "crawler_name_list" in value:
        import capo_glue.types.crawler_name_list

        out["CrawlerNameList"] = (
            capo_glue.types.crawler_name_list.serialize_aws_json_1_1(
                value["crawler_name_list"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlerMetricsRequest:
    out: GetCrawlerMetricsRequest = {}  # type: ignore[typeddict-item]
    if "CrawlerNameList" in data:
        import capo_glue.types.crawler_name_list

        out["crawler_name_list"] = (
            capo_glue.types.crawler_name_list.deserialize_aws_json_1_1(
                data["CrawlerNameList"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
