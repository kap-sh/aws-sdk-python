"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#DimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.dimension

DimensionList: TypeAlias = list["capo_marketplace_agreement.types.dimension.Dimension"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionList) -> list:
    import capo_marketplace_agreement.types.dimension

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.dimension.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DimensionList:
    import capo_marketplace_agreement.types.dimension

    out: DimensionList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.dimension.deserialize_aws_json_1_0(item)
        )
    return out
