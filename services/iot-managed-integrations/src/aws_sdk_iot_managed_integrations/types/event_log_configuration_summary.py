"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EventLogConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.log_configuration_id
    import aws_sdk_iot_managed_integrations.types.log_level
    import aws_sdk_iot_managed_integrations.types.smart_home_resource_id
    import aws_sdk_iot_managed_integrations.types.smart_home_resource_type


class EventLogConfigurationSummary(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    ]
    """<p>The identifier of the event log configuration.</p>"""
    resource_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType"
    ]
    """<p>The type of resource for the event log configuration.</p>"""
    resource_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
    ]
    """<p>The identifier of the resource for the event log configuration.</p>"""
    event_log_level: NotRequired[
        "aws_sdk_iot_managed_integrations.types.log_level.LogLevel"
    ]
    """<p>The logging level for the event log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventLogConfigurationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "event_log_level" in value:
        import aws_sdk_iot_managed_integrations.types.log_level

        out["EventLogLevel"] = (
            aws_sdk_iot_managed_integrations.types.log_level.serialize_json(
                value["event_log_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventLogConfigurationSummary:
    out: EventLogConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "EventLogLevel" in data:
        import aws_sdk_iot_managed_integrations.types.log_level

        out["event_log_level"] = (
            aws_sdk_iot_managed_integrations.types.log_level.deserialize_json(
                data["EventLogLevel"]
            )
        )
    return out
