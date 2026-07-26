"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp


class CoverageDateFilter(TypedDict, closed=True):
    start_inclusive: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>A timestamp representing the start of the time period to filter results by.</p>"""
    end_inclusive: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>A timestamp representing the end of the time period to filter results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageDateFilter) -> dict:
    out: dict = {}
    if "start_inclusive" in value:
        import capo_inspector2.types.date_time_timestamp

        out["startInclusive"] = (
            capo_inspector2.types.date_time_timestamp.serialize_json(
                value["start_inclusive"]
            )
        )
    if "end_inclusive" in value:
        import capo_inspector2.types.date_time_timestamp

        out["endInclusive"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["end_inclusive"]
        )
    return out


def deserialize_json(data: dict) -> CoverageDateFilter:
    out: CoverageDateFilter = {}  # type: ignore[typeddict-item]
    if "startInclusive" in data:
        import capo_inspector2.types.date_time_timestamp

        out["start_inclusive"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["startInclusive"]
            )
        )
    if "endInclusive" in data:
        import capo_inspector2.types.date_time_timestamp

        out["end_inclusive"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["endInclusive"]
            )
        )
    return out
