"""Generated from Smithy shape ``com.amazonaws.notifications#AggregationDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_notifications.types.summarization_dimension_details

class AggregationDetail(TypedDict):
    summarization_dimensions: NotRequired["aws_sdk_notifications.types.summarization_dimension_details.SummarizationDimensionDetails"]
    """<p>Properties used to summarize aggregated events.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AggregationDetail) -> dict:
    out: dict = {}
    if "summarization_dimensions" in value:
        import aws_sdk_notifications.types.summarization_dimension_details
        out["summarizationDimensions"] = aws_sdk_notifications.types.summarization_dimension_details.serialize_json(value["summarization_dimensions"])
    return out


def deserialize_json(data: dict) -> AggregationDetail:
    out: AggregationDetail = {}  # type: ignore[typeddict-item]
    if "summarizationDimensions" in data:
        import aws_sdk_notifications.types.summarization_dimension_details
        out["summarization_dimensions"] = aws_sdk_notifications.types.summarization_dimension_details.deserialize_json(data["summarizationDimensions"])
    return out