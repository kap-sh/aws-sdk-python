"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListEventLogConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.event_log_configuration_list_definition
    import aws_sdk_iot_managed_integrations.types.next_token


class ListEventLogConfigurationsResponse(TypedDict):
    event_log_configuration_list: NotRequired[
        "aws_sdk_iot_managed_integrations.types.event_log_configuration_list_definition.EventLogConfigurationListDefinition"
    ]
    """<p>A list of each event log configuration and pertinent information.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventLogConfigurationsResponse) -> dict:
    out: dict = {}
    if "event_log_configuration_list" in value:
        import aws_sdk_iot_managed_integrations.types.event_log_configuration_list_definition

        out["EventLogConfigurationList"] = (
            aws_sdk_iot_managed_integrations.types.event_log_configuration_list_definition.serialize_json(
                value["event_log_configuration_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventLogConfigurationsResponse:
    out: ListEventLogConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "EventLogConfigurationList" in data:
        import aws_sdk_iot_managed_integrations.types.event_log_configuration_list_definition

        out["event_log_configuration_list"] = (
            aws_sdk_iot_managed_integrations.types.event_log_configuration_list_definition.deserialize_json(
                data["EventLogConfigurationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
