"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceConnectEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ip_address_type
    import capo_ec2.types.security_group_id_string_list_request
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.tag_specification_list


class CreateInstanceConnectEndpointRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to create the EC2 Instance Connect Endpoint.</p>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.security_group_id_string_list_request.SecurityGroupIdStringListRequest"
    ]
    """<p>One or more security groups to associate with the endpoint. If you don't specify a security group, the default security group for your VPC will be associated with the endpoint.</p>"""
    preserve_client_ip: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client IP address is preserved as the source. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the client IP address as the source.</p> </li> <li> <p> <code>false</code> - Use the network interface IP address as the source.</p> </li> </ul> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note> <p>Default: <code>false</code> </p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the EC2 Instance Connect Endpoint during creation.</p>"""
    ip_address_type: NotRequired["capo_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type of the endpoint.</p> <p>If no value is specified, the default value is determined by the IP address type of the subnet:</p> <ul> <li> <p> <code>dualstack</code> - If the subnet has both IPv4 and IPv6 CIDRs</p> </li> <li> <p> <code>ipv4</code> - If the subnet has only IPv4 CIDRs</p> </li> <li> <p> <code>ipv6</code> - If the subnet has only IPv6 CIDRs</p> </li> </ul> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceConnectEndpointRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
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
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "ip_address_type" in value:
        import capo_ec2.types.ip_address_type

        capo_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )


def deserialize_ec2_query(el: Element) -> CreateInstanceConnectEndpointRequest:
    out: CreateInstanceConnectEndpointRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
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
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_ec2.types.ip_address_type

        out["ip_address_type"] = capo_ec2.types.ip_address_type.deserialize_ec2_query(
            child_ip_address_type
        )
    return out
