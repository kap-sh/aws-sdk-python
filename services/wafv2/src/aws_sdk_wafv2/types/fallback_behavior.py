"""Generated from Smithy shape ``com.amazonaws.wafv2#FallbackBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

FallbackBehavior: TypeAlias = Literal[
    "MATCH",
    "NO_MATCH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MATCH",
        "NO_MATCH",
    )
)


def serialize_aws_json_1_1(value: FallbackBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FallbackBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FallbackBehavior value: {data!r}")
    return cast(FallbackBehavior, data)
