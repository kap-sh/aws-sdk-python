"""Generated from Smithy shape ``com.amazonaws.glue#LastCrawlStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

LastCrawlStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "CANCELLED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: LastCrawlStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastCrawlStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastCrawlStatus value: {data!r}")
    return cast(LastCrawlStatus, data)
