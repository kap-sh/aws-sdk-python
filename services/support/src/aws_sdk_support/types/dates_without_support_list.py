"""Generated from Smithy shape ``com.amazonaws.support#DatesWithoutSupportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.date_interval

DatesWithoutSupportList: TypeAlias = list[
    "aws_sdk_support.types.date_interval.DateInterval"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatesWithoutSupportList) -> list:
    import aws_sdk_support.types.date_interval

    out: list = []
    for item in value:
        out.append(aws_sdk_support.types.date_interval.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DatesWithoutSupportList:
    import aws_sdk_support.types.date_interval

    out: DatesWithoutSupportList = []
    for item in data:
        out.append(aws_sdk_support.types.date_interval.deserialize_aws_json_1_1(item))
    return out
