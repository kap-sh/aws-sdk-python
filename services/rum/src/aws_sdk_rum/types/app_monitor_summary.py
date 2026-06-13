"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_id
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.app_monitor_platform
    import aws_sdk_rum.types.iso_timestamp_string
    import aws_sdk_rum.types.state_enum


class AppMonitorSummary(TypedDict):
    name: NotRequired["aws_sdk_rum.types.app_monitor_name.AppMonitorName"]
    """<p>The name of this app monitor.</p>"""
    id: NotRequired["aws_sdk_rum.types.app_monitor_id.AppMonitorId"]
    """<p>The unique ID of this app monitor.</p>"""
    created: NotRequired["aws_sdk_rum.types.iso_timestamp_string.ISOTimestampString"]
    """<p>The date and time that the app monitor was created.</p>"""
    last_modified: NotRequired[
        "aws_sdk_rum.types.iso_timestamp_string.ISOTimestampString"
    ]
    """<p>The date and time of the most recent changes to this app monitor's configuration.</p>"""
    state: NotRequired["aws_sdk_rum.types.state_enum.StateEnum"]
    """<p>The current state of this app monitor.</p>"""
    platform: NotRequired["aws_sdk_rum.types.app_monitor_platform.AppMonitorPlatform"]
    """<p>The platform type for this app monitor. Valid values are <code>Web</code> for web applications, <code>Android</code> for Android applications, and <code>iOS</code> for IOS applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppMonitorSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "created" in value:
        out["Created"] = value["created"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "state" in value:
        out["State"] = value["state"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> AppMonitorSummary:
    out: AppMonitorSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Created" in data:
        out["created"] = data["Created"]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    if "State" in data:
        out["state"] = data["State"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    return out
