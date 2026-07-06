"""Generated from Smithy shape ``com.amazonaws.ec2#Ec2InstanceConnectEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint_state
    import aws_sdk_ec2.types.instance_connect_endpoint_id
    import aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_interface_id_set
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.security_group_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_id


class Ec2InstanceConnectEndpoint(TypedDict, closed=True):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that created the EC2 Instance Connect Endpoint.</p>"""
    instance_connect_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_id.InstanceConnectEndpointId"
    ]
    """<p>The ID of the EC2 Instance Connect Endpoint.</p>"""
    instance_connect_endpoint_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the EC2 Instance Connect Endpoint.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ec2_instance_connect_endpoint_state.Ec2InstanceConnectEndpointState"
    ]
    """<p>The current state of the EC2 Instance Connect Endpoint.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The message for the current state of the EC2 Instance Connect Endpoint. Can include a failure message.</p>"""
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name of the EC2 Instance Connect Endpoint.</p>"""
    fips_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Federal Information Processing Standards (FIPS) compliant DNS name of the EC2 Instance Connect Endpoint.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.network_interface_id_set.NetworkInterfaceIdSet"
    ]
    """<p>The ID of the elastic network interface that Amazon EC2 automatically created when creating the EC2 Instance Connect Endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC in which the EC2 Instance Connect Endpoint was created.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the EC2 Instance Connect Endpoint.</p>"""
    created_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the EC2 Instance Connect Endpoint was created.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which the EC2 Instance Connect Endpoint was created.</p>"""
    preserve_client_ip: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether your client's IP address is preserved as the source when you connect to a resource. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the IP address of the client. Your instance must have an IPv4 address.</p> </li> <li> <p> <code>false</code> - Use the IP address of the network interface.</p> </li> </ul> <p>Default: <code>false</code> </p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_set.SecurityGroupIdSet"
    ]
    """<p>The security groups associated with the endpoint. If you didn't specify a security group, the default security group for your VPC is associated with the endpoint.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the EC2 Instance Connect Endpoint.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type of the endpoint.</p>"""
    public_dns_names: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names.InstanceConnectEndpointPublicDnsNames"
    ]
    """<p>The public DNS names of the endpoint.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the EC2 Instance Connect Endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ec2InstanceConnectEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "instance_connect_endpoint_id" in value:
        pairs.append(
            (
                f"{prefix}.InstanceConnectEndpointId",
                str(value["instance_connect_endpoint_id"]),
            )
        )
    if "instance_connect_endpoint_arn" in value:
        pairs.append(
            (
                f"{prefix}.InstanceConnectEndpointArn",
                str(value["instance_connect_endpoint_arn"]),
            )
        )
    if "state" in value:
        import aws_sdk_ec2.types.ec2_instance_connect_endpoint_state

        aws_sdk_ec2.types.ec2_instance_connect_endpoint_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_message" in value:
        pairs.append((f"{prefix}.StateMessage", str(value["state_message"])))
    if "dns_name" in value:
        pairs.append((f"{prefix}.DnsName", str(value["dns_name"])))
    if "fips_dns_name" in value:
        pairs.append((f"{prefix}.FipsDnsName", str(value["fips_dns_name"])))
    if "network_interface_ids" in value:
        import aws_sdk_ec2.types.network_interface_id_set

        aws_sdk_ec2.types.network_interface_id_set.serialize_ec2_query(
            value["network_interface_ids"], pairs, f"{prefix}.NetworkInterfaceIdSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "created_at" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["created_at"], pairs, f"{prefix}.CreatedAt"
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "preserve_client_ip" in value:
        pairs.append(
            (
                f"{prefix}.PreserveClientIp",
                "true" if value["preserve_client_ip"] else "false",
            )
        )
    if "security_group_ids" in value:
        import aws_sdk_ec2.types.security_group_id_set

        aws_sdk_ec2.types.security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIdSet"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "ip_address_type" in value:
        import aws_sdk_ec2.types.ip_address_type

        aws_sdk_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "public_dns_names" in value:
        import aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names

        aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names.serialize_ec2_query(
            value["public_dns_names"], pairs, f"{prefix}.PublicDnsNames"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> Ec2InstanceConnectEndpoint:
    out: Ec2InstanceConnectEndpoint = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_instance_connect_endpoint_id = el.find("InstanceConnectEndpointId")
    if child_instance_connect_endpoint_id is not None:
        out["instance_connect_endpoint_id"] = str(
            child_instance_connect_endpoint_id.text or ""
        )
    child_instance_connect_endpoint_arn = el.find("InstanceConnectEndpointArn")
    if child_instance_connect_endpoint_arn is not None:
        out["instance_connect_endpoint_arn"] = str(
            child_instance_connect_endpoint_arn.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ec2_instance_connect_endpoint_state

        out["state"] = (
            aws_sdk_ec2.types.ec2_instance_connect_endpoint_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_message = el.find("StateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_dns_name = el.find("DnsName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_fips_dns_name = el.find("FipsDnsName")
    if child_fips_dns_name is not None:
        out["fips_dns_name"] = str(child_fips_dns_name.text or "")
    if el.find("NetworkInterfaceIdSet") is not None:
        import aws_sdk_ec2.types.network_interface_id_set

        out["network_interface_ids"] = (
            aws_sdk_ec2.types.network_interface_id_set.deserialize_ec2_query(
                el, "NetworkInterfaceIdSet"
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["created_at"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_created_at
            )
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_preserve_client_ip = el.find("PreserveClientIp")
    if child_preserve_client_ip is not None:
        out["preserve_client_ip"] = (
            child_preserve_client_ip.text or ""
        ).lower() == "true"
    if el.find("SecurityGroupIdSet") is not None:
        import aws_sdk_ec2.types.security_group_id_set

        out["security_group_ids"] = (
            aws_sdk_ec2.types.security_group_id_set.deserialize_ec2_query(
                el, "SecurityGroupIdSet"
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import aws_sdk_ec2.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_ec2.types.ip_address_type.deserialize_ec2_query(
                child_ip_address_type
            )
        )
    child_public_dns_names = el.find("PublicDnsNames")
    if child_public_dns_names is not None:
        import aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names

        out["public_dns_names"] = (
            aws_sdk_ec2.types.instance_connect_endpoint_public_dns_names.deserialize_ec2_query(
                child_public_dns_names
            )
        )
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
