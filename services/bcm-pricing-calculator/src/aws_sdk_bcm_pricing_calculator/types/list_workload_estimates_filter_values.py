"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesFilterValues``."""

from typing import TypeAlias

ListWorkloadEstimatesFilterValues: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkloadEstimatesFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ListWorkloadEstimatesFilterValues:
    return list(data)
