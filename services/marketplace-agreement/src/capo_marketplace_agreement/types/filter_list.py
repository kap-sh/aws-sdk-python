"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.filter

FilterList: TypeAlias = list["capo_marketplace_agreement.types.filter.Filter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterList) -> list:
    import capo_marketplace_agreement.types.filter

    out: list = []
    for item in value:
        out.append(capo_marketplace_agreement.types.filter.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FilterList:
    import capo_marketplace_agreement.types.filter

    out: FilterList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.filter.deserialize_aws_json_1_0(item)
        )
    return out
