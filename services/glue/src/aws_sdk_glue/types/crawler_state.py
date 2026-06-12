"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CrawlerState: TypeAlias = Literal[
    "READY",
    "RUNNING",
    "STOPPING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "RUNNING",
        "STOPPING",
    )
)


def serialize_aws_json_1_1(value: CrawlerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrawlerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrawlerState value: {data!r}")
    return cast(CrawlerState, data)
