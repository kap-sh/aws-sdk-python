"""Generated from Smithy shape ``com.amazonaws.glue#CompactionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

CompactionStrategy: TypeAlias = Literal[
    "binpack",
    "sort",
    "z-order",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "binpack",
        "sort",
        "z-order",
    )
)


def serialize_aws_json_1_1(value: CompactionStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompactionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompactionStrategy value: {data!r}")
    return cast(CompactionStrategy, data)
