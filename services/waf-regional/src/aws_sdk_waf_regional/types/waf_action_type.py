"""Generated from Smithy shape ``com.amazonaws.wafregional#WafActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf_regional.errors import DeserializationError

WafActionType: TypeAlias = Literal[
    "BLOCK",
    "ALLOW",
    "COUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "ALLOW",
        "COUNT",
    )
)


def serialize_aws_json_1_1(value: WafActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WafActionType value: {data!r}")
    return cast(WafActionType, data)
