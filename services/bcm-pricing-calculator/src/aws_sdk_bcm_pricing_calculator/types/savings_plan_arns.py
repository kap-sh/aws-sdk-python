"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#SavingsPlanArns``."""

from typing import TypeAlias

SavingsPlanArns: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlanArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SavingsPlanArns:
    return list(data)
