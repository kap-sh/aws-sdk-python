"""Generated from Smithy shape ``com.amazonaws.glue#RecrawlBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

RecrawlBehavior: TypeAlias = Literal[
    "CRAWL_EVERYTHING",
    "CRAWL_NEW_FOLDERS_ONLY",
    "CRAWL_EVENT_MODE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRAWL_EVERYTHING",
        "CRAWL_NEW_FOLDERS_ONLY",
        "CRAWL_EVENT_MODE",
    )
)


def serialize_aws_json_1_1(value: RecrawlBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecrawlBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecrawlBehavior value: {data!r}")
    return cast(RecrawlBehavior, data)
