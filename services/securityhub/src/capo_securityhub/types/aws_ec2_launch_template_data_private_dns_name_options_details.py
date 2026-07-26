"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails(TypedDict, closed=True):
    enable_resource_name_dns_aaaa_record: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p> Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. </p>"""
    enable_resource_name_dns_a_record: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p> Indicates whether to respond to DNS queries for instance hostnames with DNS A records. </p>"""
    hostname_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of hostname for EC2 instances. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails) -> dict:
    out: dict = {}
    if "enable_resource_name_dns_aaaa_record" in value:
        out["EnableResourceNameDnsAAAARecord"] = value[
            "enable_resource_name_dns_aaaa_record"
        ]
    if "enable_resource_name_dns_a_record" in value:
        out["EnableResourceNameDnsARecord"] = value["enable_resource_name_dns_a_record"]
    if "hostname_type" in value:
        out["HostnameType"] = value["hostname_type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails:
    out: AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails = {}  # type: ignore[typeddict-item]
    if "EnableResourceNameDnsAAAARecord" in data:
        out["enable_resource_name_dns_aaaa_record"] = data[
            "EnableResourceNameDnsAAAARecord"
        ]
    if "EnableResourceNameDnsARecord" in data:
        out["enable_resource_name_dns_a_record"] = data["EnableResourceNameDnsARecord"]
    if "HostnameType" in data:
        out["hostname_type"] = data["HostnameType"]
    return out
