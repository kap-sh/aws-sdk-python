"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentBehaviors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.recency_dimension


class SegmentBehaviors(TypedDict, closed=True):
    recency: NotRequired["capo_pinpoint.types.recency_dimension.RecencyDimension"]
    """<p>The dimension settings that are based on how recently an endpoint was active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentBehaviors) -> dict:
    out: dict = {}
    if "recency" in value:
        import capo_pinpoint.types.recency_dimension

        out["Recency"] = capo_pinpoint.types.recency_dimension.serialize_json(
            value["recency"]
        )
    return out


def deserialize_json(data: dict) -> SegmentBehaviors:
    out: SegmentBehaviors = {}  # type: ignore[typeddict-item]
    if "Recency" in data:
        import capo_pinpoint.types.recency_dimension

        out["recency"] = capo_pinpoint.types.recency_dimension.deserialize_json(
            data["Recency"]
        )
    return out
