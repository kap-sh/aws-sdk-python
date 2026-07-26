"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfaceIpV6AddressDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2NetworkInterfaceIpV6AddressDetail(TypedDict, closed=True):
    ip_v6_address: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPV6 address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfaceIpV6AddressDetail) -> dict:
    out: dict = {}
    if "ip_v6_address" in value:
        out["IpV6Address"] = value["ip_v6_address"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkInterfaceIpV6AddressDetail:
    out: AwsEc2NetworkInterfaceIpV6AddressDetail = {}  # type: ignore[typeddict-item]
    if "IpV6Address" in data:
        out["ip_v6_address"] = data["IpV6Address"]
    return out
