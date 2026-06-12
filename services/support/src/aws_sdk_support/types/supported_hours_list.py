"""Generated from Smithy shape ``com.amazonaws.support#SupportedHoursList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.supported_hour

SupportedHoursList: TypeAlias = list[
    "aws_sdk_support.types.supported_hour.SupportedHour"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedHoursList) -> list:
    import aws_sdk_support.types.supported_hour

    out: list = []
    for item in value:
        out.append(aws_sdk_support.types.supported_hour.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedHoursList:
    import aws_sdk_support.types.supported_hour

    out: SupportedHoursList = []
    for item in data:
        out.append(aws_sdk_support.types.supported_hour.deserialize_aws_json_1_1(item))
    return out
