"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#NetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.instance_network_interface_specification

NetworkInterfaces: TypeAlias = list["aws_sdk_workspaces_instances.types.instance_network_interface_specification.InstanceNetworkInterfaceSpecification"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterfaces) -> list:
    import aws_sdk_workspaces_instances.types.instance_network_interface_specification
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_instances.types.instance_network_interface_specification.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> NetworkInterfaces:
    import aws_sdk_workspaces_instances.types.instance_network_interface_specification
    out: NetworkInterfaces = []
    for item in data:
        out.append(aws_sdk_workspaces_instances.types.instance_network_interface_specification.deserialize_aws_json_1_0(item))
    return out