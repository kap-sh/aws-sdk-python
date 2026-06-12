"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerHistoryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CrawlerHistoryState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: CrawlerHistoryState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlerHistoryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrawlerHistoryState value: {data!r}")
    return cast(CrawlerHistoryState, data)
