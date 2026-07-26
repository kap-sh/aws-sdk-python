"""Generated from Smithy shape ``com.amazonaws.quicksight#VPCConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.network_interface_list
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.security_group_id_list
    import capo_quicksight.types.string
    import capo_quicksight.types.string_list
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.vpc_connection_availability_status
    import capo_quicksight.types.vpc_connection_resource_id_unrestricted
    import capo_quicksight.types.vpc_connection_resource_status


class VPCConnection(TypedDict, closed=True):
    vpc_connection_id: NotRequired[
        "capo_quicksight.types.vpc_connection_resource_id_unrestricted.VPCConnectionResourceIdUnrestricted"
    ]
    """<p>The ID of the VPC connection that you're creating. This ID is a unique identifier for each Amazon Web Services Region in an Amazon Web Services account.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the VPC connection.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>The display name for the VPC connection.</p>"""
    vpc_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon EC2 VPC ID associated with the VPC connection.</p>"""
    security_group_ids: NotRequired[
        "capo_quicksight.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The Amazon EC2 security group IDs associated with the VPC connection.</p>"""
    dns_resolvers: NotRequired["capo_quicksight.types.string_list.StringList"]
    """<p>A list of IP addresses of DNS resolver endpoints for the VPC connection.</p>"""
    status: NotRequired[
        "capo_quicksight.types.vpc_connection_resource_status.VPCConnectionResourceStatus"
    ]
    """<p>The status of the VPC connection.</p>"""
    availability_status: NotRequired[
        "capo_quicksight.types.vpc_connection_availability_status.VPCConnectionAvailabilityStatus"
    ]
    """<p>The availability status of the VPC connection.</p>"""
    network_interfaces: NotRequired[
        "capo_quicksight.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>A list of network interfaces.</p>"""
    role_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ARN of the IAM role associated with the VPC connection.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the VPC connection was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the VPC connection was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCConnection) -> dict:
    out: dict = {}
    if "vpc_connection_id" in value:
        out["VPCConnectionId"] = value["vpc_connection_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "vpc_id" in value:
        out["VPCId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import capo_quicksight.types.security_group_id_list

        out["SecurityGroupIds"] = (
            capo_quicksight.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "dns_resolvers" in value:
        import capo_quicksight.types.string_list

        out["DnsResolvers"] = capo_quicksight.types.string_list.serialize_json(
            value["dns_resolvers"]
        )
    if "status" in value:
        import capo_quicksight.types.vpc_connection_resource_status

        out["Status"] = (
            capo_quicksight.types.vpc_connection_resource_status.serialize_json(
                value["status"]
            )
        )
    if "availability_status" in value:
        import capo_quicksight.types.vpc_connection_availability_status

        out["AvailabilityStatus"] = (
            capo_quicksight.types.vpc_connection_availability_status.serialize_json(
                value["availability_status"]
            )
        )
    if "network_interfaces" in value:
        import capo_quicksight.types.network_interface_list

        out["NetworkInterfaces"] = (
            capo_quicksight.types.network_interface_list.serialize_json(
                value["network_interfaces"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> VPCConnection:
    out: VPCConnection = {}  # type: ignore[typeddict-item]
    if "VPCConnectionId" in data:
        out["vpc_connection_id"] = data["VPCConnectionId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VPCId" in data:
        out["vpc_id"] = data["VPCId"]
    if "SecurityGroupIds" in data:
        import capo_quicksight.types.security_group_id_list

        out["security_group_ids"] = (
            capo_quicksight.types.security_group_id_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "DnsResolvers" in data:
        import capo_quicksight.types.string_list

        out["dns_resolvers"] = capo_quicksight.types.string_list.deserialize_json(
            data["DnsResolvers"]
        )
    if "Status" in data:
        import capo_quicksight.types.vpc_connection_resource_status

        out["status"] = (
            capo_quicksight.types.vpc_connection_resource_status.deserialize_json(
                data["Status"]
            )
        )
    if "AvailabilityStatus" in data:
        import capo_quicksight.types.vpc_connection_availability_status

        out["availability_status"] = (
            capo_quicksight.types.vpc_connection_availability_status.deserialize_json(
                data["AvailabilityStatus"]
            )
        )
    if "NetworkInterfaces" in data:
        import capo_quicksight.types.network_interface_list

        out["network_interfaces"] = (
            capo_quicksight.types.network_interface_list.deserialize_json(
                data["NetworkInterfaces"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
