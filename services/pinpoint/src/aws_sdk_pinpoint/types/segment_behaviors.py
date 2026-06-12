"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentBehaviors``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.recency_dimension


class SegmentBehaviors(TypedDict):
    recency: NotRequired["aws_sdk_pinpoint.types.recency_dimension.RecencyDimension"]
    """<p>The dimension settings that are based on how recently an endpoint was active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentBehaviors) -> dict:
    out: dict = {}
    if "recency" in value:
        import aws_sdk_pinpoint.types.recency_dimension

        out["Recency"] = aws_sdk_pinpoint.types.recency_dimension.serialize_json(
            value["recency"]
        )
    return out


def deserialize_json(data: dict) -> SegmentBehaviors:
    out: SegmentBehaviors = {}  # type: ignore[typeddict-item]
    if "Recency" in data:
        import aws_sdk_pinpoint.types.recency_dimension

        out["recency"] = aws_sdk_pinpoint.types.recency_dimension.deserialize_json(
            data["Recency"]
        )
    return out
