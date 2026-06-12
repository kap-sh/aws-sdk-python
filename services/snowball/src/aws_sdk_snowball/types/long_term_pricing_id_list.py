"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.long_term_pricing_id

LongTermPricingIdList: TypeAlias = list[
    "aws_sdk_snowball.types.long_term_pricing_id.LongTermPricingId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LongTermPricingIdList:
    return list(data)
