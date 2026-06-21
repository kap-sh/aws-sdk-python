"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesFilterName``."""

from typing import Literal, TypeAlias, cast

ListWorkloadEstimatesFilterName: TypeAlias = Literal[
    "STATUS",
    "NAME",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimatesFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListWorkloadEstimatesFilterName:
    return cast(ListWorkloadEstimatesFilterName, data)
