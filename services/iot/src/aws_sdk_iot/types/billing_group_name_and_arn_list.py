"""Generated from Smithy shape ``com.amazonaws.iot#BillingGroupNameAndArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.group_name_and_arn

BillingGroupNameAndArnList: TypeAlias = list[
    "aws_sdk_iot.types.group_name_and_arn.GroupNameAndArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupNameAndArnList) -> list:
    import aws_sdk_iot.types.group_name_and_arn

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.group_name_and_arn.serialize_json(item))
    return out


def deserialize_json(data: list) -> BillingGroupNameAndArnList:
    import aws_sdk_iot.types.group_name_and_arn

    out: BillingGroupNameAndArnList = []
    for item in data:
        out.append(aws_sdk_iot.types.group_name_and_arn.deserialize_json(item))
    return out
