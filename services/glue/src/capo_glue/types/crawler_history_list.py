"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.crawler_history

CrawlerHistoryList: TypeAlias = list["capo_glue.types.crawler_history.CrawlerHistory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerHistoryList) -> list:
    import capo_glue.types.crawler_history

    out: list = []
    for item in value:
        out.append(capo_glue.types.crawler_history.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CrawlerHistoryList:
    import capo_glue.types.crawler_history

    out: CrawlerHistoryList = []
    for item in data:
        out.append(capo_glue.types.crawler_history.deserialize_aws_json_1_1(item))
    return out
