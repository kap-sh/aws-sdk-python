"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessRuleEffect``."""

from typing import Literal, TypeAlias, cast

MobileDeviceAccessRuleEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessRuleEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MobileDeviceAccessRuleEffect:
    return cast(MobileDeviceAccessRuleEffect, data)
