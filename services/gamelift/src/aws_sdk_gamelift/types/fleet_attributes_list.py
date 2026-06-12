"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_attributes

FleetAttributesList: TypeAlias = list[
    "aws_sdk_gamelift.types.fleet_attributes.FleetAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAttributesList) -> list:
    import aws_sdk_gamelift.types.fleet_attributes

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.fleet_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetAttributesList:
    import aws_sdk_gamelift.types.fleet_attributes

    out: FleetAttributesList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.fleet_attributes.deserialize_aws_json_1_1(item)
        )
    return out
