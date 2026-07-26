"""Generated from Smithy shape ``com.amazonaws.mediaconnect#WindowMaintenanceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class WindowMaintenanceSchedule(TypedDict, closed=True):
    start: "datetime.datetime"
    """<p>The start time of the maintenance window.</p>"""
    end: "datetime.datetime"
    """<p>The end time of the maintenance window.</p>"""
    scheduled_time: "datetime.datetime"
    """<p>The date and time when the maintenance window is scheduled to occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WindowMaintenanceSchedule) -> dict:
    out: dict = {}
    import capo_mediaconnect.types._prelude.timestamp

    out["start"] = capo_mediaconnect.types._prelude.timestamp.serialize_json(
        value["start"]
    )
    import capo_mediaconnect.types._prelude.timestamp

    out["end"] = capo_mediaconnect.types._prelude.timestamp.serialize_json(value["end"])
    import capo_mediaconnect.types._prelude.timestamp

    out["scheduledTime"] = capo_mediaconnect.types._prelude.timestamp.serialize_json(
        value["scheduled_time"]
    )
    return out


def deserialize_json(data: dict) -> WindowMaintenanceSchedule:
    out: WindowMaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if "start" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["start"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["start"]
        )
    else:
        raise DeserializationError("WindowMaintenanceSchedule.start required")
    if "end" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["end"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["end"]
        )
    else:
        raise DeserializationError("WindowMaintenanceSchedule.end required")
    if "scheduledTime" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["scheduled_time"] = (
            capo_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["scheduledTime"]
            )
        )
    else:
        raise DeserializationError("WindowMaintenanceSchedule.scheduled_time required")
    return out
