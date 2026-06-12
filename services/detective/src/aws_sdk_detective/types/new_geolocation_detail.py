"""Generated from Smithy shape ``com.amazonaws.detective#NewGeolocationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.ip_address
    import aws_sdk_detective.types.is_new_for_entire_account
    import aws_sdk_detective.types.location


class NewGeolocationDetail(TypedDict):
    location: NotRequired["aws_sdk_detective.types.location.Location"]
    """<p>Location where the resource was accessed.</p>"""
    ip_address: NotRequired["aws_sdk_detective.types.ip_address.IpAddress"]
    """<p>IP address using which the resource was accessed.</p>"""
    is_new_for_entire_account: (
        "aws_sdk_detective.types.is_new_for_entire_account.IsNewForEntireAccount"
    )
    """<p>Checks if the geolocation is new for the entire account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewGeolocationDetail) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    out["IsNewForEntireAccount"] = value.get("is_new_for_entire_account", False)
    return out


def deserialize_json(data: dict) -> NewGeolocationDetail:
    out: NewGeolocationDetail = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        out["location"] = data["Location"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "IsNewForEntireAccount" in data:
        out["is_new_for_entire_account"] = data["IsNewForEntireAccount"]
    else:
        out["is_new_for_entire_account"] = False
    return out
