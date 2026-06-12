"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.destination_name
    import aws_sdk_iot_managed_integrations.types.event_type
    import aws_sdk_iot_managed_integrations.types.tags_map


class CreateNotificationConfigurationRequest(TypedDict):
    event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType"
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""
    destination_name: (
        "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName"
    )
    """<p>The name of the destination for the notification configuration.</p>"""
    client_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    tags: NotRequired["aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.event_type

    out["EventType"] = aws_sdk_iot_managed_integrations.types.event_type.serialize_json(
        value["event_type"]
    )
    out["DestinationName"] = value["destination_name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["Tags"] = aws_sdk_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNotificationConfigurationRequest:
    out: CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        import aws_sdk_iot_managed_integrations.types.event_type

        out["event_type"] = (
            aws_sdk_iot_managed_integrations.types.event_type.deserialize_json(
                data["EventType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationRequest.event_type required"
        )
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationRequest.destination_name required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["tags"] = aws_sdk_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out
