"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenariosFilterName``."""

from typing import Literal, TypeAlias, cast

ListBillScenariosFilterName: TypeAlias = Literal[
    "STATUS",
    "NAME",
    "GROUP_SHARING_PREFERENCE",
    "COST_CATEGORY_ARN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillScenariosFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListBillScenariosFilterName:
    return cast(ListBillScenariosFilterName, data)
