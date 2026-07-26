"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerState``."""

from typing import Literal, TypeAlias, cast

CrawlerState: TypeAlias = Literal[
    "READY",
    "RUNNING",
    "STOPPING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlerState:
    return cast(CrawlerState, data)
