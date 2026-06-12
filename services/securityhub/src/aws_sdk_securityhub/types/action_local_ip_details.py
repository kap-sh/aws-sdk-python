"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionLocalIpDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class ActionLocalIpDetails(TypedDict):
    ip_address_v4: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionLocalIpDetails) -> dict:
    out: dict = {}
    if "ip_address_v4" in value:
        out["IpAddressV4"] = value["ip_address_v4"]
    return out


def deserialize_json(data: dict) -> ActionLocalIpDetails:
    out: ActionLocalIpDetails = {}  # type: ignore[typeddict-item]
    if "IpAddressV4" in data:
        out["ip_address_v4"] = data["IpAddressV4"]
    return out
