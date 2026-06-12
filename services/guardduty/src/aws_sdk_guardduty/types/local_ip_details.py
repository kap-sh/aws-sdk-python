"""Generated from Smithy shape ``com.amazonaws.guardduty#LocalIpDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.sensitive_string


class LocalIpDetails(TypedDict):
    ip_address_v4: NotRequired[
        "aws_sdk_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The IPv4 local address of the connection.</p>"""
    ip_address_v6: NotRequired[
        "aws_sdk_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The IPv6 local address of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalIpDetails) -> dict:
    out: dict = {}
    if "ip_address_v4" in value:
        out["ipAddressV4"] = value["ip_address_v4"]
    if "ip_address_v6" in value:
        out["ipAddressV6"] = value["ip_address_v6"]
    return out


def deserialize_json(data: dict) -> LocalIpDetails:
    out: LocalIpDetails = {}  # type: ignore[typeddict-item]
    if "ipAddressV4" in data:
        out["ip_address_v4"] = data["ipAddressV4"]
    if "ipAddressV6" in data:
        out["ip_address_v6"] = data["ipAddressV6"]
    return out
