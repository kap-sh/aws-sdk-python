"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.filter_value

FilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.filter_value.FilterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FilterValueList:
    return list(data)
