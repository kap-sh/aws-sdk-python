"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerLineageSettings``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CrawlerLineageSettings: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
    )
)


def serialize_aws_json_1_1(value: CrawlerLineageSettings) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlerLineageSettings:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrawlerLineageSettings value: {data!r}")
    return cast(CrawlerLineageSettings, data)
