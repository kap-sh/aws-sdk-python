"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceConnectEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_connect_endpoint_id
    import capo_ec2.types.ip_address_type
    import capo_ec2.types.security_group_id_string_list_request


class ModifyInstanceConnectEndpointRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_connect_endpoint_id: NotRequired[
        "capo_ec2.types.instance_connect_endpoint_id.InstanceConnectEndpointId"
    ]
    """<p>The ID of the EC2 Instance Connect Endpoint to modify.</p>"""
    ip_address_type: NotRequired["capo_ec2.types.ip_address_type.IpAddressType"]
    """<p>The new IP address type for the EC2 Instance Connect Endpoint.</p> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.security_group_id_string_list_request.SecurityGroupIdStringListRequest"
    ]
    """<p>Changes the security groups for the EC2 Instance Connect Endpoint. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.</p>"""
    preserve_client_ip: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client IP address is preserved as the source when you connect to a resource. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the IP address of the client. Your instance must have an IPv4 address.</p> </li> <li> <p> <code>false</code> - Use the IP address of the network interface.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceConnectEndpointRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_connect_endpoint_id" in value:
        pairs.append(
            (
                f"{prefix}.InstanceConnectEndpointId",
                str(value["instance_connect_endpoint_id"]),
            )
        )
    if "ip_address_type" in value:
        import capo_ec2.types.ip_address_type

        capo_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "security_group_ids" in value:
        import capo_ec2.types.security_group_id_string_list_request

        capo_ec2.types.security_group_id_string_list_request.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "preserve_client_ip" in value:
        pairs.append(
            (
                f"{prefix}.PreserveClientIp",
                "true" if value["preserve_client_ip"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceConnectEndpointRequest:
    out: ModifyInstanceConnectEndpointRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_connect_endpoint_id = el.find("InstanceConnectEndpointId")
    if child_instance_connect_endpoint_id is not None:
        out["instance_connect_endpoint_id"] = str(
            child_instance_connect_endpoint_id.text or ""
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_ec2.types.ip_address_type

        out["ip_address_type"] = capo_ec2.types.ip_address_type.deserialize_ec2_query(
            child_ip_address_type
        )
    if el.find("SecurityGroupIds") is not None:
        import capo_ec2.types.security_group_id_string_list_request

        out["security_group_ids"] = (
            capo_ec2.types.security_group_id_string_list_request.deserialize_ec2_query(
                el, "SecurityGroupIds"
            )
        )
    child_preserve_client_ip = el.find("PreserveClientIp")
    if child_preserve_client_ip is not None:
        out["preserve_client_ip"] = (
            child_preserve_client_ip.text or ""
        ).lower() == "true"
    return out
