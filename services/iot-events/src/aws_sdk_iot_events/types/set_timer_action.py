"""Generated from Smithy shape ``com.amazonaws.iotevents#SetTimerAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.seconds
    import aws_sdk_iot_events.types.timer_name
    import aws_sdk_iot_events.types.variable_value


class SetTimerAction(TypedDict):
    timer_name: "aws_sdk_iot_events.types.timer_name.TimerName"
    """<p>The name of the timer.</p>"""
    seconds: NotRequired["aws_sdk_iot_events.types.seconds.Seconds"]
    """<p>The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds. </p>"""
    duration_expression: NotRequired[
        "aws_sdk_iot_events.types.variable_value.VariableValue"
    ]
    """<p>The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (<code>$variable.<variable-name></code>), and input values (<code>$input.<input-name>.<path-to-datum></code>) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetTimerAction) -> dict:
    out: dict = {}
    out["timerName"] = value["timer_name"]
    if "seconds" in value:
        out["seconds"] = value["seconds"]
    if "duration_expression" in value:
        out["durationExpression"] = value["duration_expression"]
    return out


def deserialize_json(data: dict) -> SetTimerAction:
    out: SetTimerAction = {}  # type: ignore[typeddict-item]
    if "timerName" in data:
        out["timer_name"] = data["timerName"]
    else:
        raise DeserializationError("SetTimerAction.timer_name required")
    if "seconds" in data:
        out["seconds"] = data["seconds"]
    if "durationExpression" in data:
        out["duration_expression"] = data["durationExpression"]
    return out
