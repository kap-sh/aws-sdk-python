"""Generated from Smithy shape ``com.amazonaws.lightsail#BehaviorEnum``."""

from typing import Literal, TypeAlias, cast

BehaviorEnum: TypeAlias = Literal[
    "dont-cache",
    "cache",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BehaviorEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BehaviorEnum:
    return cast(BehaviorEnum, data)
