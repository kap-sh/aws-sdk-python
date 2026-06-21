"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RevenueModel``."""

from typing import Literal, TypeAlias, cast

RevenueModel: TypeAlias = Literal[
    "Contract",
    "Pay-as-you-go",
    "Subscription",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RevenueModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RevenueModel:
    return cast(RevenueModel, data)
