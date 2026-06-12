"""Generated from Smithy shape ``com.amazonaws.wafv2#RateBasedStatementAggregateKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

RateBasedStatementAggregateKeyType: TypeAlias = Literal[
    "IP",
    "FORWARDED_IP",
    "CUSTOM_KEYS",
    "CONSTANT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IP",
        "FORWARDED_IP",
        "CUSTOM_KEYS",
        "CONSTANT",
    )
)


def serialize_aws_json_1_1(value: RateBasedStatementAggregateKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RateBasedStatementAggregateKeyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RateBasedStatementAggregateKeyType value: {data!r}"
        )
    return cast(RateBasedStatementAggregateKeyType, data)
