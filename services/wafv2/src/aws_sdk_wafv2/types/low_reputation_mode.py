"""Generated from Smithy shape ``com.amazonaws.wafv2#LowReputationMode``."""

from typing import Literal, TypeAlias, cast

LowReputationMode: TypeAlias = Literal[
    "ACTIVE_UNDER_DDOS",
    "ALWAYS_ON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LowReputationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LowReputationMode:
    return cast(LowReputationMode, data)
