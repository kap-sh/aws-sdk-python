"""Generated from Smithy shape ``com.amazonaws.pinpoint#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__double
    import aws_sdk_pinpoint.types.map_of__string
    import aws_sdk_pinpoint.types.session


class Event(TypedDict, closed=True):
    app_package_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The package name of the app that's recording the event.</p>"""
    app_title: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The title of the app that's recording the event.</p>"""
    app_version_code: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The version number of the app that's recording the event.</p>"""
    attributes: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>One or more custom attributes that are associated with the event.</p>"""
    client_sdk_version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The version of the SDK that's running on the client device.</p>"""
    event_type: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the event.</p>"""
    metrics: NotRequired["aws_sdk_pinpoint.types.map_of__double.MapOf__double"]
    """<p>One or more custom metrics that are associated with the event.</p>"""
    sdk_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the SDK that's being used to record the event.</p>"""
    session: NotRequired["aws_sdk_pinpoint.types.session.Session"]
    """<p>Information about the session in which the event occurred.</p>"""
    timestamp: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the event occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    if "app_package_name" in value:
        out["AppPackageName"] = value["app_package_name"]
    if "app_title" in value:
        out["AppTitle"] = value["app_title"]
    if "app_version_code" in value:
        out["AppVersionCode"] = value["app_version_code"]
    if "attributes" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Attributes"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["attributes"]
        )
    if "client_sdk_version" in value:
        out["ClientSdkVersion"] = value["client_sdk_version"]
    if "event_type" in value:
        out["EventType"] = value["event_type"]
    if "metrics" in value:
        import aws_sdk_pinpoint.types.map_of__double

        out["Metrics"] = aws_sdk_pinpoint.types.map_of__double.serialize_json(
            value["metrics"]
        )
    if "sdk_name" in value:
        out["SdkName"] = value["sdk_name"]
    if "session" in value:
        import aws_sdk_pinpoint.types.session

        out["Session"] = aws_sdk_pinpoint.types.session.serialize_json(value["session"])
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "AppPackageName" in data:
        out["app_package_name"] = data["AppPackageName"]
    if "AppTitle" in data:
        out["app_title"] = data["AppTitle"]
    if "AppVersionCode" in data:
        out["app_version_code"] = data["AppVersionCode"]
    if "Attributes" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["attributes"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Attributes"]
        )
    if "ClientSdkVersion" in data:
        out["client_sdk_version"] = data["ClientSdkVersion"]
    if "EventType" in data:
        out["event_type"] = data["EventType"]
    if "Metrics" in data:
        import aws_sdk_pinpoint.types.map_of__double

        out["metrics"] = aws_sdk_pinpoint.types.map_of__double.deserialize_json(
            data["Metrics"]
        )
    if "SdkName" in data:
        out["sdk_name"] = data["SdkName"]
    if "Session" in data:
        import aws_sdk_pinpoint.types.session

        out["session"] = aws_sdk_pinpoint.types.session.deserialize_json(
            data["Session"]
        )
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    return out
