"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DetectorStateDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.state_name
    import aws_sdk_iot_events_data.types.timer_definitions
    import aws_sdk_iot_events_data.types.variable_definitions


class DetectorStateDefinition(TypedDict, closed=True):
    state_name: "aws_sdk_iot_events_data.types.state_name.StateName"
    """<p>The name of the new state of the detector (instance).</p>"""
    variables: "aws_sdk_iot_events_data.types.variable_definitions.VariableDefinitions"
    """<p>The new values of the detector's variables. Any variable whose value isn't specified is cleared.</p>"""
    timers: "aws_sdk_iot_events_data.types.timer_definitions.TimerDefinitions"
    """<p>The new values of the detector's timers. Any timer whose value isn't specified is cleared, and its timeout event won't occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorStateDefinition) -> dict:
    out: dict = {}
    out["stateName"] = value["state_name"]
    import aws_sdk_iot_events_data.types.variable_definitions

    out["variables"] = (
        aws_sdk_iot_events_data.types.variable_definitions.serialize_json(
            value["variables"]
        )
    )
    import aws_sdk_iot_events_data.types.timer_definitions

    out["timers"] = aws_sdk_iot_events_data.types.timer_definitions.serialize_json(
        value["timers"]
    )
    return out


def deserialize_json(data: dict) -> DetectorStateDefinition:
    out: DetectorStateDefinition = {}  # type: ignore[typeddict-item]
    if "stateName" in data:
        out["state_name"] = data["stateName"]
    else:
        raise DeserializationError("DetectorStateDefinition.state_name required")
    if "variables" in data:
        import aws_sdk_iot_events_data.types.variable_definitions

        out["variables"] = (
            aws_sdk_iot_events_data.types.variable_definitions.deserialize_json(
                data["variables"]
            )
        )
    else:
        raise DeserializationError("DetectorStateDefinition.variables required")
    if "timers" in data:
        import aws_sdk_iot_events_data.types.timer_definitions

        out["timers"] = (
            aws_sdk_iot_events_data.types.timer_definitions.deserialize_json(
                data["timers"]
            )
        )
    else:
        raise DeserializationError("DetectorStateDefinition.timers required")
    return out
