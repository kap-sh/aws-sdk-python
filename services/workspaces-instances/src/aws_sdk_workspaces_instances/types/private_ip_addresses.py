"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PrivateIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.private_ip_address_specification

PrivateIpAddresses: TypeAlias = list[
    "aws_sdk_workspaces_instances.types.private_ip_address_specification.PrivateIpAddressSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivateIpAddresses) -> list:
    import aws_sdk_workspaces_instances.types.private_ip_address_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_instances.types.private_ip_address_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PrivateIpAddresses:
    import aws_sdk_workspaces_instances.types.private_ip_address_specification

    out: PrivateIpAddresses = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.private_ip_address_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out
