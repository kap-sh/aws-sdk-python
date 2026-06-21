"""Generated from Smithy shape ``com.amazonaws.glue#CrawlState``."""

from typing import Literal, TypeAlias, cast

CrawlState: TypeAlias = Literal[
    "RUNNING",
    "CANCELLING",
    "CANCELLED",
    "SUCCEEDED",
    "FAILED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlState:
    return cast(CrawlState, data)
