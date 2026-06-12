"""Generated from Smithy shape ``com.amazonaws.wafv2#Scope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

Scope: TypeAlias = Literal[
    "CLOUDFRONT",
    "REGIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDFRONT",
        "REGIONAL",
    )
)


def serialize_aws_json_1_1(value: Scope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Scope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scope value: {data!r}")
    return cast(Scope, data)
