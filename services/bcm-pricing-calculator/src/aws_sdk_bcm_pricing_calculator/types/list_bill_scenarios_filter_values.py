"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenariosFilterValues``."""

from typing import TypeAlias

ListBillScenariosFilterValues: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillScenariosFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ListBillScenariosFilterValues:
    return list(data)
