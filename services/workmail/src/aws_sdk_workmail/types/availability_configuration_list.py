"""Generated from Smithy shape ``com.amazonaws.workmail#AvailabilityConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.availability_configuration

AvailabilityConfigurationList: TypeAlias = list[
    "aws_sdk_workmail.types.availability_configuration.AvailabilityConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityConfigurationList) -> list:
    import aws_sdk_workmail.types.availability_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.availability_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AvailabilityConfigurationList:
    import aws_sdk_workmail.types.availability_configuration

    out: AvailabilityConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.availability_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
