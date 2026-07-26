"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateLineItemsFilterName``."""

from typing import Literal, TypeAlias, cast

ListBillEstimateLineItemsFilterName: TypeAlias = Literal[
    "USAGE_ACCOUNT_ID",
    "SERVICE_CODE",
    "USAGE_TYPE",
    "OPERATION",
    "LOCATION",
    "LINE_ITEM_TYPE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimateLineItemsFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListBillEstimateLineItemsFilterName:
    return cast(ListBillEstimateLineItemsFilterName, data)
