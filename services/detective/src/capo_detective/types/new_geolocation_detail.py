"""Generated from Smithy shape ``com.amazonaws.detective#NewGeolocationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.ip_address
    import capo_detective.types.is_new_for_entire_account
    import capo_detective.types.location


class NewGeolocationDetail(TypedDict, closed=True):
    location: NotRequired["capo_detective.types.location.Location"]
    """<p>Location where the resource was accessed.</p>"""
    ip_address: NotRequired["capo_detective.types.ip_address.IpAddress"]
    """<p>IP address using which the resource was accessed.</p>"""
    is_new_for_entire_account: (
        "capo_detective.types.is_new_for_entire_account.IsNewForEntireAccount"
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
