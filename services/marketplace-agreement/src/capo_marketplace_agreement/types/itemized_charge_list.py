"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ItemizedChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.itemized_charge

ItemizedChargeList: TypeAlias = list[
    "capo_marketplace_agreement.types.itemized_charge.ItemizedCharge"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemizedChargeList) -> list:
    import capo_marketplace_agreement.types.itemized_charge

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.itemized_charge.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ItemizedChargeList:
    import capo_marketplace_agreement.types.itemized_charge

    out: ItemizedChargeList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.itemized_charge.deserialize_aws_json_1_0(
                item
            )
        )
    return out
