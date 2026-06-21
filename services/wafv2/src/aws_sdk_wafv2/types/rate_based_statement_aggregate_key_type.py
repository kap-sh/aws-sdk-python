"""Generated from Smithy shape ``com.amazonaws.wafv2#RateBasedStatementAggregateKeyType``."""

from typing import Literal, TypeAlias, cast

RateBasedStatementAggregateKeyType: TypeAlias = Literal[
    "IP",
    "FORWARDED_IP",
    "CUSTOM_KEYS",
    "CONSTANT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateBasedStatementAggregateKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RateBasedStatementAggregateKeyType:
    return cast(RateBasedStatementAggregateKeyType, data)
