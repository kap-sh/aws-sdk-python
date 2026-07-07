"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.acknowledge_flow
    import aws_sdk_iot_events.types.initialization_configuration


class AlarmCapabilities(TypedDict, closed=True):
    initialization_configuration: NotRequired[
        "aws_sdk_iot_events.types.initialization_configuration.InitializationConfiguration"
    ]
    """<p>Specifies the default alarm state. The configuration applies to all alarms that were created based on this alarm model.</p>"""
    acknowledge_flow: NotRequired[
        "aws_sdk_iot_events.types.acknowledge_flow.AcknowledgeFlow"
    ]
    """<p>Specifies whether to get notified for alarm state changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmCapabilities) -> dict:
    out: dict = {}
    if "initialization_configuration" in value:
        import aws_sdk_iot_events.types.initialization_configuration

        out["initializationConfiguration"] = (
            aws_sdk_iot_events.types.initialization_configuration.serialize_json(
                value["initialization_configuration"]
            )
        )
    if "acknowledge_flow" in value:
        import aws_sdk_iot_events.types.acknowledge_flow

        out["acknowledgeFlow"] = (
            aws_sdk_iot_events.types.acknowledge_flow.serialize_json(
                value["acknowledge_flow"]
            )
        )
    return out


def deserialize_json(data: dict) -> AlarmCapabilities:
    out: AlarmCapabilities = {}  # type: ignore[typeddict-item]
    if "initializationConfiguration" in data:
        import aws_sdk_iot_events.types.initialization_configuration

        out["initialization_configuration"] = (
            aws_sdk_iot_events.types.initialization_configuration.deserialize_json(
                data["initializationConfiguration"]
            )
        )
    if "acknowledgeFlow" in data:
        import aws_sdk_iot_events.types.acknowledge_flow

        out["acknowledge_flow"] = (
            aws_sdk_iot_events.types.acknowledge_flow.deserialize_json(
                data["acknowledgeFlow"]
            )
        )
    return out
