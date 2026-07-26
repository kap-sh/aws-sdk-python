"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionRoutesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2VpnConnectionRoutesDetails(TypedDict, closed=True):
    destination_cidr_block: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The CIDR block associated with the local subnet of the customer data center.</p>"""
    state: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current state of the static route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionRoutesDetails) -> dict:
    out: dict = {}
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpnConnectionRoutesDetails:
    out: AwsEc2VpnConnectionRoutesDetails = {}  # type: ignore[typeddict-item]
    if "DestinationCidrBlock" in data:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if "State" in data:
        out["state"] = data["State"]
    return out
