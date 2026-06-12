"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.location_configuration

LocationConfigurationList: TypeAlias = list[
    "aws_sdk_gamelift.types.location_configuration.LocationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationConfigurationList) -> list:
    import aws_sdk_gamelift.types.location_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.location_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LocationConfigurationList:
    import aws_sdk_gamelift.types.location_configuration

    out: LocationConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.location_configuration.deserialize_aws_json_1_1(item)
        )
    return out
