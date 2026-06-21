"""Generated from Smithy shape ``com.amazonaws.emr#MarketType``."""

from typing import Literal, TypeAlias, cast

MarketType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MarketType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MarketType:
    return cast(MarketType, data)
