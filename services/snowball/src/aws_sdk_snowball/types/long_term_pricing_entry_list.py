"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.long_term_pricing_list_entry

LongTermPricingEntryList: TypeAlias = list[
    "aws_sdk_snowball.types.long_term_pricing_list_entry.LongTermPricingListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingEntryList) -> list:
    import aws_sdk_snowball.types.long_term_pricing_list_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snowball.types.long_term_pricing_list_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LongTermPricingEntryList:
    import aws_sdk_snowball.types.long_term_pricing_list_entry

    out: LongTermPricingEntryList = []
    for item in data:
        out.append(
            aws_sdk_snowball.types.long_term_pricing_list_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
