"""Generated from Smithy shape ``com.amazonaws.glue#ResourceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ResourceState: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCESS",
    "STOPPED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "SUCCESS",
        "STOPPED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ResourceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceState value: {data!r}")
    return cast(ResourceState, data)
