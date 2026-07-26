"""Generated from Smithy shape ``com.amazonaws.glue#RecrawlBehavior``."""

from typing import Literal, TypeAlias, cast

RecrawlBehavior: TypeAlias = Literal[
    "CRAWL_EVERYTHING",
    "CRAWL_NEW_FOLDERS_ONLY",
    "CRAWL_EVENT_MODE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecrawlBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecrawlBehavior:
    return cast(RecrawlBehavior, data)
