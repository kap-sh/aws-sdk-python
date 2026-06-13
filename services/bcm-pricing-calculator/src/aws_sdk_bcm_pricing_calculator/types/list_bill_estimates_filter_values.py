"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimatesFilterValues``."""

from typing import TypeAlias

ListBillEstimatesFilterValues: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimatesFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ListBillEstimatesFilterValues:
    return list(data)
