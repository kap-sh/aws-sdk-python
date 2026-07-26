"""Generated from Smithy shape ``com.amazonaws.iot#GetCardinalityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.count


class GetCardinalityResponse(TypedDict, closed=True):
    cardinality: "capo_iot.types.count.Count"
    """<p>The approximate count of unique values that match the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCardinalityResponse) -> dict:
    out: dict = {}
    out["cardinality"] = value.get("cardinality", 0)
    return out


def deserialize_json(data: dict) -> GetCardinalityResponse:
    out: GetCardinalityResponse = {}  # type: ignore[typeddict-item]
    if "cardinality" in data:
        out["cardinality"] = data["cardinality"]
    else:
        out["cardinality"] = 0
    return out
