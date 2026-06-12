"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Ipv6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.instance_ipv6_address

Ipv6Addresses: TypeAlias = list["aws_sdk_workspaces_instances.types.instance_ipv6_address.InstanceIpv6Address"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv6Addresses) -> list:
    import aws_sdk_workspaces_instances.types.instance_ipv6_address
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_instances.types.instance_ipv6_address.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Ipv6Addresses:
    import aws_sdk_workspaces_instances.types.instance_ipv6_address
    out: Ipv6Addresses = []
    for item in data:
        out.append(aws_sdk_workspaces_instances.types.instance_ipv6_address.deserialize_aws_json_1_0(item))
    return out