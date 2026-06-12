"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler

CrawlerList: TypeAlias = list["aws_sdk_glue.types.crawler.Crawler"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerList) -> list:
    import aws_sdk_glue.types.crawler

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.crawler.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CrawlerList:
    import aws_sdk_glue.types.crawler

    out: CrawlerList = []
    for item in data:
        out.append(aws_sdk_glue.types.crawler.deserialize_aws_json_1_1(item))
    return out
