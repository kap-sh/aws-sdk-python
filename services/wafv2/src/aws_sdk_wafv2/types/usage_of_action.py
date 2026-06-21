"""Generated from Smithy shape ``com.amazonaws.wafv2#UsageOfAction``."""

from typing import Literal, TypeAlias, cast

UsageOfAction: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageOfAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageOfAction:
    return cast(UsageOfAction, data)
