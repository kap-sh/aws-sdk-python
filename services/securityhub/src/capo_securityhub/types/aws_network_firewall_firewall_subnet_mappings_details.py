"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsNetworkFirewallFirewallSubnetMappingsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsNetworkFirewallFirewallSubnetMappingsDetails(TypedDict, closed=True):
    subnet_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the subnet</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsNetworkFirewallFirewallSubnetMappingsDetails) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> AwsNetworkFirewallFirewallSubnetMappingsDetails:
    out: AwsNetworkFirewallFirewallSubnetMappingsDetails = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    return out
