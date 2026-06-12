"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerNodeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawl_list


class CrawlerNodeDetails(TypedDict):
    crawls: NotRequired["aws_sdk_glue.types.crawl_list.CrawlList"]
    """<p>A list of crawls represented by the crawl node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerNodeDetails) -> dict:
    out: dict = {}
    if "crawls" in value:
        import aws_sdk_glue.types.crawl_list

        out["Crawls"] = aws_sdk_glue.types.crawl_list.serialize_aws_json_1_1(
            value["crawls"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlerNodeDetails:
    out: CrawlerNodeDetails = {}  # type: ignore[typeddict-item]
    if "Crawls" in data:
        import aws_sdk_glue.types.crawl_list

        out["crawls"] = aws_sdk_glue.types.crawl_list.deserialize_aws_json_1_1(
            data["Crawls"]
        )
    return out
