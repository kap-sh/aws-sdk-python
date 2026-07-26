"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsNameOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.hostname_type


class PrivateDnsNameOptionsResponse(TypedDict, closed=True):
    hostname_type: NotRequired["capo_ec2.types.hostname_type.HostnameType"]
    """<p>The type of hostname to assign to an instance.</p>"""
    enable_resource_name_dns_a_record: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsNameOptionsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hostname_type" in value:
        import capo_ec2.types.hostname_type

        capo_ec2.types.hostname_type.serialize_ec2_query(
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


def deserialize_ec2_query(el: Element) -> PrivateDnsNameOptionsResponse:
    out: PrivateDnsNameOptionsResponse = {}  # type: ignore[typeddict-item]
    child_hostname_type = el.find("HostnameType")
    if child_hostname_type is not None:
        import capo_ec2.types.hostname_type

        out["hostname_type"] = capo_ec2.types.hostname_type.deserialize_ec2_query(
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
