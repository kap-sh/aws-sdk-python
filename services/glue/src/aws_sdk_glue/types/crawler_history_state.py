"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerHistoryState``."""

from typing import Literal, TypeAlias, cast

CrawlerHistoryState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerHistoryState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlerHistoryState:
    return cast(CrawlerHistoryState, data)
