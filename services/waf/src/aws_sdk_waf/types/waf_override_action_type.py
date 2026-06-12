"""Generated from Smithy shape ``com.amazonaws.waf#WafOverrideActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

WafOverrideActionType: TypeAlias = Literal[
    "NONE",
    "COUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "COUNT",
    )
)


def serialize_aws_json_1_1(value: WafOverrideActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafOverrideActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WafOverrideActionType value: {data!r}")
    return cast(WafOverrideActionType, data)
