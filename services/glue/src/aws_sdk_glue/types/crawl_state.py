"""Generated from Smithy shape ``com.amazonaws.glue#CrawlState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CrawlState: TypeAlias = Literal[
    "RUNNING",
    "CANCELLING",
    "CANCELLED",
    "SUCCEEDED",
    "FAILED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: CrawlState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrawlState value: {data!r}")
    return cast(CrawlState, data)
