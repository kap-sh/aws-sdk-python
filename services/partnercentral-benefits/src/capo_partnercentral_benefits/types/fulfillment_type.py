"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FulfillmentType``."""

from typing import Literal, TypeAlias, cast

FulfillmentType: TypeAlias = Literal[
    "CREDITS",
    "CASH",
    "ACCESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FulfillmentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FulfillmentType:
    return cast(FulfillmentType, data)
