"""Generated from Smithy shape ``com.amazonaws.wafregional#WafRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf_regional.errors import DeserializationError

WafRuleType: TypeAlias = Literal[
    "REGULAR",
    "RATE_BASED",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGULAR",
        "RATE_BASED",
        "GROUP",
    )
)


def serialize_aws_json_1_1(value: WafRuleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WafRuleType value: {data!r}")
    return cast(WafRuleType, data)
