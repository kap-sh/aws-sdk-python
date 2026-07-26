"""Generated from Smithy shape ``com.amazonaws.forecast#LongArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.long_arn

LongArnList: TypeAlias = list["capo_forecast.types.long_arn.LongArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LongArnList:
    return list(data)
