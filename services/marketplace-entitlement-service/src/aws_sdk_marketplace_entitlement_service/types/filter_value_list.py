"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_entitlement_service.types.filter_value

FilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_entitlement_service.types.filter_value.FilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilterValueList:
    return list(data)
