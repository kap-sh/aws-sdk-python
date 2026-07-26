"""Generated from Smithy shape ``com.amazonaws.glue#CrawlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.crawl

CrawlList: TypeAlias = list["capo_glue.types.crawl.Crawl"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlList) -> list:
    import capo_glue.types.crawl

    out: list = []
    for item in value:
        out.append(capo_glue.types.crawl.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CrawlList:
    import capo_glue.types.crawl

    out: CrawlList = []
    for item in data:
        out.append(capo_glue.types.crawl.deserialize_aws_json_1_1(item))
    return out
