"""Generated from Smithy shape ``com.amazonaws.kendra#WebCrawlerMode``."""

from typing import Literal, TypeAlias, cast

WebCrawlerMode: TypeAlias = Literal[
    "HOST_ONLY",
    "SUBDOMAINS",
    "EVERYTHING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebCrawlerMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebCrawlerMode:
    return cast(WebCrawlerMode, data)
