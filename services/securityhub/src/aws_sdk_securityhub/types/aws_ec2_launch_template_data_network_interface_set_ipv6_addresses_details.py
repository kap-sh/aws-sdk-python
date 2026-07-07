"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails(
    TypedDict, closed=True
):
    ipv6_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails,
) -> dict:
    out: dict = {}
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails:
    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails = {}  # type: ignore[typeddict-item]
    if "Ipv6Address" in data:
        out["ipv6_address"] = data["Ipv6Address"]
    return out
