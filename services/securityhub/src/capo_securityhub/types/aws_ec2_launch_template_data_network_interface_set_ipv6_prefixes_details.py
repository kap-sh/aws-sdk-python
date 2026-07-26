"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails(
    TypedDict, closed=True
):
    ipv6_prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The IPv6 prefix. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails,
) -> dict:
    out: dict = {}
    if "ipv6_prefix" in value:
        out["Ipv6Prefix"] = value["ipv6_prefix"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails:
    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails = {}  # type: ignore[typeddict-item]
    if "Ipv6Prefix" in data:
        out["ipv6_prefix"] = data["Ipv6Prefix"]
    return out
