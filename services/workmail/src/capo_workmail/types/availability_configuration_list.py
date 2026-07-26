"""Generated from Smithy shape ``com.amazonaws.workmail#AvailabilityConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.availability_configuration

AvailabilityConfigurationList: TypeAlias = list[
    "capo_workmail.types.availability_configuration.AvailabilityConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityConfigurationList) -> list:
    import capo_workmail.types.availability_configuration

    out: list = []
    for item in value:
        out.append(
            capo_workmail.types.availability_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AvailabilityConfigurationList:
    import capo_workmail.types.availability_configuration

    out: AvailabilityConfigurationList = []
    for item in data:
        out.append(
            capo_workmail.types.availability_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
