"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Timestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date

Timestamps: TypeAlias = list["aws_sdk_cloudtrail.types.date.Date"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Timestamps) -> list:
    import aws_sdk_cloudtrail.types.date

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Timestamps:
    import aws_sdk_cloudtrail.types.date

    out: Timestamps = []
    for item in data:
        out.append(aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(item))
    return out
