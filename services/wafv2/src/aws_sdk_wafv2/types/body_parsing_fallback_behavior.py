"""Generated from Smithy shape ``com.amazonaws.wafv2#BodyParsingFallbackBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

BodyParsingFallbackBehavior: TypeAlias = Literal[
    "MATCH",
    "NO_MATCH",
    "EVALUATE_AS_STRING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MATCH",
        "NO_MATCH",
        "EVALUATE_AS_STRING",
    )
)


def serialize_aws_json_1_1(value: BodyParsingFallbackBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BodyParsingFallbackBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BodyParsingFallbackBehavior value: {data!r}"
        )
    return cast(BodyParsingFallbackBehavior, data)
