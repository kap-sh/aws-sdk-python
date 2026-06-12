"""Generated from Smithy shape ``com.amazonaws.wafv2#FailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

FailureReason: TypeAlias = Literal[
    "TOKEN_MISSING",
    "TOKEN_EXPIRED",
    "TOKEN_INVALID",
    "TOKEN_DOMAIN_MISMATCH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOKEN_MISSING",
        "TOKEN_EXPIRED",
        "TOKEN_INVALID",
        "TOKEN_DOMAIN_MISMATCH",
    )
)


def serialize_aws_json_1_1(value: FailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureReason value: {data!r}")
    return cast(FailureReason, data)
