"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.log_level
    import aws_sdk_iot_managed_integrations.types.smart_home_resource_id
    import aws_sdk_iot_managed_integrations.types.smart_home_resource_type


class CreateEventLogConfigurationRequest(TypedDict, closed=True):
    resource_type: "aws_sdk_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType"
    """<p>The type of resource for the event log configuration.</p>"""
    resource_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
    ]
    """<p>The identifier of the resource for the event log configuration.</p>"""
    event_log_level: "aws_sdk_iot_managed_integrations.types.log_level.LogLevel"
    """<p>The logging level for the event log configuration.</p>"""
    client_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventLogConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    import aws_sdk_iot_managed_integrations.types.log_level

    out["EventLogLevel"] = (
        aws_sdk_iot_managed_integrations.types.log_level.serialize_json(
            value["event_log_level"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateEventLogConfigurationRequest:
    out: CreateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError(
            "CreateEventLogConfigurationRequest.resource_type required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "EventLogLevel" in data:
        import aws_sdk_iot_managed_integrations.types.log_level

        out["event_log_level"] = (
            aws_sdk_iot_managed_integrations.types.log_level.deserialize_json(
                data["EventLogLevel"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEventLogConfigurationRequest.event_log_level required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
