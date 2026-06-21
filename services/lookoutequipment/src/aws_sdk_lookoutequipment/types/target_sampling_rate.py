"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#TargetSamplingRate``."""

from typing import Literal, TypeAlias, cast

TargetSamplingRate: TypeAlias = Literal[
    "PT1S",
    "PT5S",
    "PT10S",
    "PT15S",
    "PT30S",
    "PT1M",
    "PT5M",
    "PT10M",
    "PT15M",
    "PT30M",
    "PT1H",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetSamplingRate) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TargetSamplingRate:
    return cast(TargetSamplingRate, data)
