"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateLineItemsFilterValues``."""

from typing import TypeAlias

ListBillEstimateLineItemsFilterValues: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimateLineItemsFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ListBillEstimateLineItemsFilterValues:
    return list(data)
