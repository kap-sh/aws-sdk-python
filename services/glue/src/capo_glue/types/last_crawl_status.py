"""Generated from Smithy shape ``com.amazonaws.glue#LastCrawlStatus``."""

from typing import Literal, TypeAlias, cast

LastCrawlStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastCrawlStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastCrawlStatus:
    return cast(LastCrawlStatus, data)
