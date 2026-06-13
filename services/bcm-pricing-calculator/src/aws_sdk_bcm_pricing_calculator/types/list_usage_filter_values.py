"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListUsageFilterValues``."""

from typing import TypeAlias

ListUsageFilterValues: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListUsageFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ListUsageFilterValues:
    return list(data)
