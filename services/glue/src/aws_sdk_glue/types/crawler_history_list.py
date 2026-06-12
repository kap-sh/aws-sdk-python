"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_history

CrawlerHistoryList: TypeAlias = list[
    "aws_sdk_glue.types.crawler_history.CrawlerHistory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerHistoryList) -> list:
    import aws_sdk_glue.types.crawler_history

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.crawler_history.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CrawlerHistoryList:
    import aws_sdk_glue.types.crawler_history

    out: CrawlerHistoryList = []
    for item in data:
        out.append(aws_sdk_glue.types.crawler_history.deserialize_aws_json_1_1(item))
    return out
