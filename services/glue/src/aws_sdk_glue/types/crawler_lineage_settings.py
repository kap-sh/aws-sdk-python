"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerLineageSettings``."""

from typing import Literal, TypeAlias, cast

CrawlerLineageSettings: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerLineageSettings) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlerLineageSettings:
    return cast(CrawlerLineageSettings, data)
