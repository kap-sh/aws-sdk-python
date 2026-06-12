"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfacePrivateIpAddressDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2NetworkInterfacePrivateIpAddressDetail(TypedDict):
    private_ip_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IP address.</p>"""
    private_dns_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The private DNS name for the IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfacePrivateIpAddressDetail) -> dict:
    out: dict = {}
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "private_dns_name" in value:
        out["PrivateDnsName"] = value["private_dns_name"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkInterfacePrivateIpAddressDetail:
    out: AwsEc2NetworkInterfacePrivateIpAddressDetail = {}  # type: ignore[typeddict-item]
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if "PrivateDnsName" in data:
        out["private_dns_name"] = data["PrivateDnsName"]
    return out
