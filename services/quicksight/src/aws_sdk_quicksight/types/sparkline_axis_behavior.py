"""Generated from Smithy shape ``com.amazonaws.quicksight#SparklineAxisBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SparklineAxisBehavior: TypeAlias = Literal[
    "SHARED",
    "INDEPENDENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHARED",
        "INDEPENDENT",
    )
)


def serialize_json(value: SparklineAxisBehavior) -> str:
    return value


def deserialize_json(data: str) -> SparklineAxisBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SparklineAxisBehavior value: {data!r}")
    return cast(SparklineAxisBehavior, data)
