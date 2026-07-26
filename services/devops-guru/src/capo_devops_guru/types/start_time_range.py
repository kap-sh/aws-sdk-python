"""Generated from Smithy shape ``com.amazonaws.devopsguru#StartTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.timestamp


class StartTimeRange(TypedDict, closed=True):
    from_time: NotRequired["capo_devops_guru.types.timestamp.Timestamp"]
    """<p> The start time of the time range. </p>"""
    to_time: NotRequired["capo_devops_guru.types.timestamp.Timestamp"]
    """<p> The end time of the time range. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTimeRange) -> dict:
    out: dict = {}
    if "from_time" in value:
        import capo_devops_guru.types.timestamp

        out["FromTime"] = capo_devops_guru.types.timestamp.serialize_json(
            value["from_time"]
        )
    if "to_time" in value:
        import capo_devops_guru.types.timestamp

        out["ToTime"] = capo_devops_guru.types.timestamp.serialize_json(
            value["to_time"]
        )
    return out


def deserialize_json(data: dict) -> StartTimeRange:
    out: StartTimeRange = {}  # type: ignore[typeddict-item]
    if "FromTime" in data:
        import capo_devops_guru.types.timestamp

        out["from_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    if "ToTime" in data:
        import capo_devops_guru.types.timestamp

        out["to_time"] = capo_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    return out
