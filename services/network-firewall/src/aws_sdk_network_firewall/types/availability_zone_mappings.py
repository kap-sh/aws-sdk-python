"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AvailabilityZoneMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.availability_zone_mapping

AvailabilityZoneMappings: TypeAlias = list[
    "aws_sdk_network_firewall.types.availability_zone_mapping.AvailabilityZoneMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AvailabilityZoneMappings) -> list:
    import aws_sdk_network_firewall.types.availability_zone_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.availability_zone_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AvailabilityZoneMappings:
    import aws_sdk_network_firewall.types.availability_zone_mapping

    out: AvailabilityZoneMappings = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.availability_zone_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
