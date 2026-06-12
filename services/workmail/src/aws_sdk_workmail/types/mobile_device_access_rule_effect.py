"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessRuleEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

MobileDeviceAccessRuleEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: MobileDeviceAccessRuleEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MobileDeviceAccessRuleEffect:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MobileDeviceAccessRuleEffect value: {data!r}"
        )
    return cast(MobileDeviceAccessRuleEffect, data)
