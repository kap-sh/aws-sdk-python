"""Generated from Smithy shape ``com.amazonaws.invoicing#BillingEntity``."""

from typing import Literal, TypeAlias, cast

BillingEntity: TypeAlias = Literal[
    "AWS",
    "AWS_MARKETPLACE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingEntity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingEntity:
    return cast(BillingEntity, data)
