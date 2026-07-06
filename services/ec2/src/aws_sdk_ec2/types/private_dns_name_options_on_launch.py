"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsNameOptionsOnLaunch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.hostname_type


class PrivateDnsNameOptionsOnLaunch(TypedDict, closed=True):
    hostname_type: NotRequired["aws_sdk_ec2.types.hostname_type.HostnameType"]
    """<p>The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.</p>"""
    enable_resource_name_dns_a_record: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostname with DNS AAAA records.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsNameOptionsOnLaunch, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hostname_type" in value:
        import aws_sdk_ec2.types.hostname_type

        aws_sdk_ec2.types.hostname_type.serialize_ec2_query(
            value["hostname_type"], pairs, f"{prefix}.HostnameType"
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


def deserialize_ec2_query(el: Element) -> PrivateDnsNameOptionsOnLaunch:
    out: PrivateDnsNameOptionsOnLaunch = {}  # type: ignore[typeddict-item]
    child_hostname_type = el.find("HostnameType")
    if child_hostname_type is not None:
        import aws_sdk_ec2.types.hostname_type

        out["hostname_type"] = aws_sdk_ec2.types.hostname_type.deserialize_ec2_query(
            child_hostname_type
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
