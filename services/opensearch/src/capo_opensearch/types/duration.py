"""Generated from Smithy shape ``com.amazonaws.opensearch#Duration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.duration_value
    import capo_opensearch.types.time_unit


class Duration(TypedDict, closed=True):
    value: NotRequired["capo_opensearch.types.duration_value.DurationValue"]
    """<p>Integer to specify the value of a maintenance schedule duration.</p>"""
    unit: NotRequired["capo_opensearch.types.time_unit.TimeUnit"]
    """<p>The unit of measurement for the duration of a maintenance schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Duration) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        import capo_opensearch.types.time_unit

        out["Unit"] = capo_opensearch.types.time_unit.serialize_json(value["unit"])
    return out


def deserialize_json(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Unit" in data:
        import capo_opensearch.types.time_unit

        out["unit"] = capo_opensearch.types.time_unit.deserialize_json(data["Unit"])
    return out
