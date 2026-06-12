"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.log_configuration_id
    import aws_sdk_iot_managed_integrations.types.log_level


class UpdateEventLogConfigurationRequest(TypedDict):
    id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    """<p>The log configuration id.</p>"""
    event_log_level: "aws_sdk_iot_managed_integrations.types.log_level.LogLevel"
    """<p>The log level for the event in terms of severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventLogConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.log_level

    out["EventLogLevel"] = (
        aws_sdk_iot_managed_integrations.types.log_level.serialize_json(
            value["event_log_level"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateEventLogConfigurationRequest:
    out: UpdateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "EventLogLevel" in data:
        import aws_sdk_iot_managed_integrations.types.log_level

        out["event_log_level"] = (
            aws_sdk_iot_managed_integrations.types.log_level.deserialize_json(
                data["EventLogLevel"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEventLogConfigurationRequest.event_log_level required"
        )
    return out
