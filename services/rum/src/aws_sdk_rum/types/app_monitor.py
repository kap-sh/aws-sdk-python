"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitor``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_configuration
    import aws_sdk_rum.types.app_monitor_domain
    import aws_sdk_rum.types.app_monitor_domain_list
    import aws_sdk_rum.types.app_monitor_id
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.app_monitor_platform
    import aws_sdk_rum.types.custom_events
    import aws_sdk_rum.types.data_storage
    import aws_sdk_rum.types.deobfuscation_configuration
    import aws_sdk_rum.types.iso_timestamp_string
    import aws_sdk_rum.types.state_enum
    import aws_sdk_rum.types.tag_map

class AppMonitor(TypedDict):
    name: NotRequired["aws_sdk_rum.types.app_monitor_name.AppMonitorName"]
    """<p>The name of the app monitor.</p>"""
    domain: NotRequired["aws_sdk_rum.types.app_monitor_domain.AppMonitorDomain"]
    """<p>The top-level internet domain name for which your application has administrative authority.</p>"""
    domain_list: NotRequired["aws_sdk_rum.types.app_monitor_domain_list.AppMonitorDomainList"]
    """<p> List the domain names for which your application has administrative authority. </p>"""
    id: NotRequired["aws_sdk_rum.types.app_monitor_id.AppMonitorId"]
    """<p>The unique ID of this app monitor.</p>"""
    created: NotRequired["aws_sdk_rum.types.iso_timestamp_string.ISOTimestampString"]
    """<p>The date and time that this app monitor was created.</p>"""
    last_modified: NotRequired["aws_sdk_rum.types.iso_timestamp_string.ISOTimestampString"]
    """<p>The date and time of the most recent changes to this app monitor's configuration.</p>"""
    tags: NotRequired["aws_sdk_rum.types.tag_map.TagMap"]
    """<p>The list of tag keys and values associated with this app monitor.</p>"""
    state: NotRequired["aws_sdk_rum.types.state_enum.StateEnum"]
    """<p>The current state of the app monitor.</p>"""
    app_monitor_configuration: NotRequired["aws_sdk_rum.types.app_monitor_configuration.AppMonitorConfiguration"]
    """<p>A structure that contains much of the configuration data for the app monitor.</p>"""
    data_storage: NotRequired["aws_sdk_rum.types.data_storage.DataStorage"]
    """<p>A structure that contains information about whether this app monitor stores a copy of the telemetry data that RUM collects using CloudWatch Logs.</p>"""
    custom_events: NotRequired["aws_sdk_rum.types.custom_events.CustomEvents"]
    """<p>Specifies whether this app monitor allows the web client to define and send custom events.</p> <p>For more information about custom events, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html\">Send custom events</a>.</p>"""
    deobfuscation_configuration: NotRequired["aws_sdk_rum.types.deobfuscation_configuration.DeobfuscationConfiguration"]
    """<p> A structure that contains the configuration for how an app monitor can deobfuscate stack traces. </p>"""
    platform: NotRequired["aws_sdk_rum.types.app_monitor_platform.AppMonitorPlatform"]
    """<p>The platform type for this app monitor. Valid values are <code>Web</code> for web applications , <code>Android</code> for Android applications, and <code>iOS</code> for IOS applications.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AppMonitor) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "domain_list" in value:
        import aws_sdk_rum.types.app_monitor_domain_list
        out["DomainList"] = aws_sdk_rum.types.app_monitor_domain_list.serialize_json(value["domain_list"])
    if "id" in value:
        out["Id"] = value["id"]
    if "created" in value:
        out["Created"] = value["created"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "tags" in value:
        import aws_sdk_rum.types.tag_map
        out["Tags"] = aws_sdk_rum.types.tag_map.serialize_json(value["tags"])
    if "state" in value:
        out["State"] = value["state"]
    if "app_monitor_configuration" in value:
        import aws_sdk_rum.types.app_monitor_configuration
        out["AppMonitorConfiguration"] = aws_sdk_rum.types.app_monitor_configuration.serialize_json(value["app_monitor_configuration"])
    if "data_storage" in value:
        import aws_sdk_rum.types.data_storage
        out["DataStorage"] = aws_sdk_rum.types.data_storage.serialize_json(value["data_storage"])
    if "custom_events" in value:
        import aws_sdk_rum.types.custom_events
        out["CustomEvents"] = aws_sdk_rum.types.custom_events.serialize_json(value["custom_events"])
    if "deobfuscation_configuration" in value:
        import aws_sdk_rum.types.deobfuscation_configuration
        out["DeobfuscationConfiguration"] = aws_sdk_rum.types.deobfuscation_configuration.serialize_json(value["deobfuscation_configuration"])
    if "platform" in value:
        out["Platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> AppMonitor:
    out: AppMonitor = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "DomainList" in data:
        import aws_sdk_rum.types.app_monitor_domain_list
        out["domain_list"] = aws_sdk_rum.types.app_monitor_domain_list.deserialize_json(data["DomainList"])
    if "Id" in data:
        out["id"] = data["Id"]
    if "Created" in data:
        out["created"] = data["Created"]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    if "Tags" in data:
        import aws_sdk_rum.types.tag_map
        out["tags"] = aws_sdk_rum.types.tag_map.deserialize_json(data["Tags"])
    if "State" in data:
        out["state"] = data["State"]
    if "AppMonitorConfiguration" in data:
        import aws_sdk_rum.types.app_monitor_configuration
        out["app_monitor_configuration"] = aws_sdk_rum.types.app_monitor_configuration.deserialize_json(data["AppMonitorConfiguration"])
    if "DataStorage" in data:
        import aws_sdk_rum.types.data_storage
        out["data_storage"] = aws_sdk_rum.types.data_storage.deserialize_json(data["DataStorage"])
    if "CustomEvents" in data:
        import aws_sdk_rum.types.custom_events
        out["custom_events"] = aws_sdk_rum.types.custom_events.deserialize_json(data["CustomEvents"])
    if "DeobfuscationConfiguration" in data:
        import aws_sdk_rum.types.deobfuscation_configuration
        out["deobfuscation_configuration"] = aws_sdk_rum.types.deobfuscation_configuration.deserialize_json(data["DeobfuscationConfiguration"])
    if "Platform" in data:
        out["platform"] = data["Platform"]
    return out