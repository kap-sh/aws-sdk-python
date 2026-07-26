"""Generated from Smithy shape ``com.amazonaws.mediatailor#Transition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__long
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.relative_position


class Transition(TypedDict, closed=True):
    duration_millis: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The duration of the live program in seconds.</p>"""
    relative_position: "capo_mediatailor.types.relative_position.RelativePosition"
    """<p>The position where this program will be inserted relative to the <code>RelativePosition</code>.</p>"""
    relative_program: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the program that this program will be inserted next to, as defined by <code>RelativePosition</code>.</p>"""
    scheduled_start_time_millis: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The date and time that the program is scheduled to start, in epoch milliseconds.</p>"""
    type: "capo_mediatailor.types.__string.__string"
    """<p>Defines when the program plays in the schedule. You can set the value to <code>ABSOLUTE</code> or <code>RELATIVE</code>.</p> <p> <code>ABSOLUTE</code> - The program plays at a specific wall clock time. This setting can only be used for channels using the <code>LINEAR</code> <code>PlaybackMode</code>.</p> <p>Note the following considerations when using <code>ABSOLUTE</code> transitions:</p> <p>If the preceding program in the schedule has a duration that extends past the wall clock time, MediaTailor truncates the preceding program on a common segment boundary.</p> <p>If there are gaps in playback, MediaTailor plays the <code>FillerSlate</code> you configured for your linear channel.</p> <p> <code>RELATIVE</code> - The program is inserted into the schedule either before or after a program that you specify via <code>RelativePosition</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transition) -> dict:
    out: dict = {}
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    import capo_mediatailor.types.relative_position

    out["RelativePosition"] = capo_mediatailor.types.relative_position.serialize_json(
        value["relative_position"]
    )
    if "relative_program" in value:
        out["RelativeProgram"] = value["relative_program"]
    if "scheduled_start_time_millis" in value:
        out["ScheduledStartTimeMillis"] = value["scheduled_start_time_millis"]
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Transition:
    out: Transition = {}  # type: ignore[typeddict-item]
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    if "RelativePosition" in data:
        import capo_mediatailor.types.relative_position

        out["relative_position"] = (
            capo_mediatailor.types.relative_position.deserialize_json(
                data["RelativePosition"]
            )
        )
    else:
        raise DeserializationError("Transition.relative_position required")
    if "RelativeProgram" in data:
        out["relative_program"] = data["RelativeProgram"]
    if "ScheduledStartTimeMillis" in data:
        out["scheduled_start_time_millis"] = data["ScheduledStartTimeMillis"]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("Transition.type required")
    return out
