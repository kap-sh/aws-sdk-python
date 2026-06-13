"""Generated from Smithy shape ``com.amazonaws.mailmanager#SearchState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

SearchState: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_0(value: SearchState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SearchState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchState value: {data!r}")
    return cast(SearchState, data)
