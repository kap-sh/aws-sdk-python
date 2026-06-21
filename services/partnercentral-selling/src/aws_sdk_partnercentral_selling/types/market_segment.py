"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#MarketSegment``."""

from typing import Literal, TypeAlias, cast

MarketSegment: TypeAlias = Literal[
    "Enterprise",
    "Large",
    "Medium",
    "Small",
    "Micro",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MarketSegment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketSegment:
    return cast(MarketSegment, data)
