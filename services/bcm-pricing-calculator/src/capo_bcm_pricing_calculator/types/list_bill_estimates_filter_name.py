"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimatesFilterName``."""

from typing import Literal, TypeAlias, cast

ListBillEstimatesFilterName: TypeAlias = Literal[
    "STATUS",
    "NAME",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimatesFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListBillEstimatesFilterName:
    return cast(ListBillEstimatesFilterName, data)
