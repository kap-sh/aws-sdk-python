"""Generated from Smithy shape ``com.amazonaws.wickr#BasicDeviceObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class BasicDeviceObject(TypedDict, closed=True):
    app_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The unique application ID for the Wickr app on this device.</p>"""
    created: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The timestamp when the device first appeared in the Wickr database.</p>"""
    last_login: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The timestamp when the device last successfully logged into Wickr. This is also used to determine SSO idle time.</p>"""
    status_text: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The current status of the device, either 'Active' or 'Reset' depending on whether the device is currently active or has been marked for reset.</p>"""
    suspend: NotRequired["bool"]
    """<p>Indicates whether the device is suspended.</p>"""
    type: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The operating system of the device (e.g., 'MacOSX', 'Windows', 'iOS', 'Android').</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicDeviceObject) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "created" in value:
        out["created"] = value["created"]
    if "last_login" in value:
        out["lastLogin"] = value["last_login"]
    if "status_text" in value:
        out["statusText"] = value["status_text"]
    if "suspend" in value:
        out["suspend"] = value["suspend"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> BasicDeviceObject:
    out: BasicDeviceObject = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "created" in data:
        out["created"] = data["created"]
    if "lastLogin" in data:
        out["last_login"] = data["lastLogin"]
    if "statusText" in data:
        out["status_text"] = data["statusText"]
    if "suspend" in data:
        out["suspend"] = data["suspend"]
    if "type" in data:
        out["type"] = data["type"]
    return out
