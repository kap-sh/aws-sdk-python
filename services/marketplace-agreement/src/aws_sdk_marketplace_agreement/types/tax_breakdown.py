"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TaxBreakdown``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.tax_breakdown_item

TaxBreakdown: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.tax_breakdown_item.TaxBreakdownItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxBreakdown) -> list:
    import aws_sdk_marketplace_agreement.types.tax_breakdown_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.tax_breakdown_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TaxBreakdown:
    import aws_sdk_marketplace_agreement.types.tax_breakdown_item

    out: TaxBreakdown = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.tax_breakdown_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
