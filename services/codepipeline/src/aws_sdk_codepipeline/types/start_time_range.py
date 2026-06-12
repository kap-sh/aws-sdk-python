"""Generated from Smithy shape ``com.amazonaws.codepipeline#StartTimeRange``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

StartTimeRange: TypeAlias = Literal[
    "Latest",
    "All",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Latest",
        "All",
    )
)


def serialize_aws_json_1_1(value: StartTimeRange) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StartTimeRange:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StartTimeRange value: {data!r}")
    return cast(StartTimeRange, data)
