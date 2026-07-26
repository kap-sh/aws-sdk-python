"""Generated from Smithy shape ``com.amazonaws.sustainability#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.timestamp


class TimePeriod(TypedDict, closed=True):
    start: "capo_sustainability.types.timestamp.Timestamp"
    """<p>The start (inclusive) of the time period. ISO-8601 formatted timestamp, for example: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    end: "capo_sustainability.types.timestamp.Timestamp"
    """<p>The end (exclusive) of the time period. ISO-8601 formatted timestamp, for example: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimePeriod) -> dict:
    out: dict = {}
    import capo_sustainability.types.timestamp

    out["Start"] = capo_sustainability.types.timestamp.serialize_json(value["start"])
    import capo_sustainability.types.timestamp

    out["End"] = capo_sustainability.types.timestamp.serialize_json(value["end"])
    return out


def deserialize_json(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        import capo_sustainability.types.timestamp

        out["start"] = capo_sustainability.types.timestamp.deserialize_json(
            data["Start"]
        )
    else:
        raise DeserializationError("TimePeriod.start required")
    if "End" in data:
        import capo_sustainability.types.timestamp

        out["end"] = capo_sustainability.types.timestamp.deserialize_json(data["End"])
    else:
        raise DeserializationError("TimePeriod.end required")
    return out
