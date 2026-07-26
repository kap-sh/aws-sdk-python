"""Generated from Smithy shape ``com.amazonaws.braket#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class TimePeriod(TypedDict, closed=True):
    start_at: "datetime.datetime"
    """<p>The start date and time for the spending limit period, in epoch seconds.</p>"""
    end_at: "datetime.datetime"
    """<p>The end date and time for the spending limit period, in epoch seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimePeriod) -> dict:
    out: dict = {}
    import capo_braket.types._prelude.timestamp

    out["startAt"] = capo_braket.types._prelude.timestamp.serialize_json(
        value["start_at"]
    )
    import capo_braket.types._prelude.timestamp

    out["endAt"] = capo_braket.types._prelude.timestamp.serialize_json(value["end_at"])
    return out


def deserialize_json(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if "startAt" in data:
        import capo_braket.types._prelude.timestamp

        out["start_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["startAt"]
        )
    else:
        raise DeserializationError("TimePeriod.start_at required")
    if "endAt" in data:
        import capo_braket.types._prelude.timestamp

        out["end_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["endAt"]
        )
    else:
        raise DeserializationError("TimePeriod.end_at required")
    return out
