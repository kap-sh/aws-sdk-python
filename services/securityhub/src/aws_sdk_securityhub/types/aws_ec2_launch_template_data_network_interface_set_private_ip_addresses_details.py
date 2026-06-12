"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails(TypedDict):
    primary: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary. </p>"""
    private_ip_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The private IPv4 address. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails,
) -> dict:
    out: dict = {}
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails:
    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    return out
