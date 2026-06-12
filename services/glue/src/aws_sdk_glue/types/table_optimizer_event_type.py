"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TableOptimizerEventType: TypeAlias = Literal[
    "starting",
    "completed",
    "failed",
    "in_progress",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "starting",
        "completed",
        "failed",
        "in_progress",
    )
)


def serialize_aws_json_1_1(value: TableOptimizerEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableOptimizerEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableOptimizerEventType value: {data!r}")
    return cast(TableOptimizerEventType, data)
