"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyPrivateDnsNameOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.hostname_type
    import aws_sdk_ec2.types.instance_id


class ModifyPrivateDnsNameOptionsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    private_dns_hostname_type: NotRequired[
        "aws_sdk_ec2.types.hostname_type.HostnameType"
    ]
    """<p>The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.</p>"""
    enable_resource_name_dns_a_record: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyPrivateDnsNameOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "private_dns_hostname_type" in value:
        import aws_sdk_ec2.types.hostname_type

        aws_sdk_ec2.types.hostname_type.serialize_ec2_query(
            value["private_dns_hostname_type"],
            pairs,
            f"{prefix}.PrivateDnsHostnameType",
        )
    if "enable_resource_name_dns_a_record" in value:
        pairs.append(
            (
                f"{prefix}.EnableResourceNameDnsARecord",
                "true" if value["enable_resource_name_dns_a_record"] else "false",
            )
        )
    if "enable_resource_name_dns_aaaa_record" in value:
        pairs.append(
            (
                f"{prefix}.EnableResourceNameDnsAAAARecord",
                "true" if value["enable_resource_name_dns_aaaa_record"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyPrivateDnsNameOptionsRequest:
    out: ModifyPrivateDnsNameOptionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_private_dns_hostname_type = el.find("PrivateDnsHostnameType")
    if child_private_dns_hostname_type is not None:
        import aws_sdk_ec2.types.hostname_type

        out["private_dns_hostname_type"] = (
            aws_sdk_ec2.types.hostname_type.deserialize_ec2_query(
                child_private_dns_hostname_type
            )
        )
    child_enable_resource_name_dns_a_record = el.find("EnableResourceNameDnsARecord")
    if child_enable_resource_name_dns_a_record is not None:
        out["enable_resource_name_dns_a_record"] = (
            child_enable_resource_name_dns_a_record.text or ""
        ).lower() == "true"
    child_enable_resource_name_dns_aaaa_record = el.find(
        "EnableResourceNameDnsAAAARecord"
    )
    if child_enable_resource_name_dns_aaaa_record is not None:
        out["enable_resource_name_dns_aaaa_record"] = (
            child_enable_resource_name_dns_aaaa_record.text or ""
        ).lower() == "true"
    return out
