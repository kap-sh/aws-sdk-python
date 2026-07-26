"""Generated from Smithy shape ``com.amazonaws.xray#InsightImpactGraphEdge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_integer


class InsightImpactGraphEdge(TypedDict, closed=True):
    reference_id: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>Identifier of the edge. Unique within a service map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightImpactGraphEdge) -> dict:
    out: dict = {}
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> InsightImpactGraphEdge:
    out: InsightImpactGraphEdge = {}  # type: ignore[typeddict-item]
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    return out
