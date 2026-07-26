"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetCrawlersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawler_list
    import capo_glue.types.crawler_name_list


class BatchGetCrawlersResponse(TypedDict, closed=True):
    crawlers: NotRequired["capo_glue.types.crawler_list.CrawlerList"]
    """<p>A list of crawler definitions.</p>"""
    crawlers_not_found: NotRequired["capo_glue.types.crawler_name_list.CrawlerNameList"]
    """<p>A list of names of crawlers that were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCrawlersResponse) -> dict:
    out: dict = {}
    if "crawlers" in value:
        import capo_glue.types.crawler_list

        out["Crawlers"] = capo_glue.types.crawler_list.serialize_aws_json_1_1(
            value["crawlers"]
        )
    if "crawlers_not_found" in value:
        import capo_glue.types.crawler_name_list

        out["CrawlersNotFound"] = (
            capo_glue.types.crawler_name_list.serialize_aws_json_1_1(
                value["crawlers_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCrawlersResponse:
    out: BatchGetCrawlersResponse = {}  # type: ignore[typeddict-item]
    if "Crawlers" in data:
        import capo_glue.types.crawler_list

        out["crawlers"] = capo_glue.types.crawler_list.deserialize_aws_json_1_1(
            data["Crawlers"]
        )
    if "CrawlersNotFound" in data:
        import capo_glue.types.crawler_name_list

        out["crawlers_not_found"] = (
            capo_glue.types.crawler_name_list.deserialize_aws_json_1_1(
                data["CrawlersNotFound"]
            )
        )
    return out
