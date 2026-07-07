"""Generated from Smithy shape ``com.amazonaws.iotevents#OnInputLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.events
    import aws_sdk_iot_events.types.transition_events


class OnInputLifecycle(TypedDict, closed=True):
    events: NotRequired["aws_sdk_iot_events.types.events.Events"]
    """<p>Specifies the actions performed when the <code>condition</code> evaluates to TRUE.</p>"""
    transition_events: NotRequired[
        "aws_sdk_iot_events.types.transition_events.TransitionEvents"
    ]
    """<p>Specifies the actions performed, and the next state entered, when a <code>condition</code> evaluates to TRUE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnInputLifecycle) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_iot_events.types.events

        out["events"] = aws_sdk_iot_events.types.events.serialize_json(value["events"])
    if "transition_events" in value:
        import aws_sdk_iot_events.types.transition_events

        out["transitionEvents"] = (
            aws_sdk_iot_events.types.transition_events.serialize_json(
                value["transition_events"]
            )
        )
    return out


def deserialize_json(data: dict) -> OnInputLifecycle:
    out: OnInputLifecycle = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_iot_events.types.events

        out["events"] = aws_sdk_iot_events.types.events.deserialize_json(data["events"])
    if "transitionEvents" in data:
        import aws_sdk_iot_events.types.transition_events

        out["transition_events"] = (
            aws_sdk_iot_events.types.transition_events.deserialize_json(
                data["transitionEvents"]
            )
        )
    return out
