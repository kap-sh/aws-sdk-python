"""Generated from Smithy shape ``com.amazonaws.devicefarm#RecurringChargeFrequency``."""

from typing import Literal, TypeAlias, cast

RecurringChargeFrequency: TypeAlias = Literal["MONTHLY",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurringChargeFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecurringChargeFrequency:
    return cast(RecurringChargeFrequency, data)
