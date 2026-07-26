"""Generated from Smithy shape ``com.amazonaws.invoicing#BuyerDomain``."""

from typing import Literal, TypeAlias, cast

BuyerDomain: TypeAlias = Literal["NetworkID",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerDomain) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BuyerDomain:
    return cast(BuyerDomain, data)
