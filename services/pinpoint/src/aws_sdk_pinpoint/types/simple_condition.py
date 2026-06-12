"""Generated from Smithy shape ``com.amazonaws.pinpoint#SimpleCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.event_condition
    import aws_sdk_pinpoint.types.segment_condition
    import aws_sdk_pinpoint.types.segment_dimensions


class SimpleCondition(TypedDict):
    event_condition: NotRequired[
        "aws_sdk_pinpoint.types.event_condition.EventCondition"
    ]
    """<p>The dimension settings for the event that's associated with the activity.</p>"""
    segment_condition: NotRequired[
        "aws_sdk_pinpoint.types.segment_condition.SegmentCondition"
    ]
    """<p>The segment that's associated with the activity.</p>"""
    segment_dimensions: NotRequired[
        "aws_sdk_pinpoint.types.segment_dimensions.SegmentDimensions"
    ]
    """<p>The dimension settings for the segment that's associated with the activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleCondition) -> dict:
    out: dict = {}
    if "event_condition" in value:
        import aws_sdk_pinpoint.types.event_condition

        out["EventCondition"] = aws_sdk_pinpoint.types.event_condition.serialize_json(
            value["event_condition"]
        )
    if "segment_condition" in value:
        import aws_sdk_pinpoint.types.segment_condition

        out["SegmentCondition"] = (
            aws_sdk_pinpoint.types.segment_condition.serialize_json(
                value["segment_condition"]
            )
        )
    if "segment_dimensions" in value:
        import aws_sdk_pinpoint.types.segment_dimensions

        out["segmentDimensions"] = (
            aws_sdk_pinpoint.types.segment_dimensions.serialize_json(
                value["segment_dimensions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SimpleCondition:
    out: SimpleCondition = {}  # type: ignore[typeddict-item]
    if "EventCondition" in data:
        import aws_sdk_pinpoint.types.event_condition

        out["event_condition"] = (
            aws_sdk_pinpoint.types.event_condition.deserialize_json(
                data["EventCondition"]
            )
        )
    if "SegmentCondition" in data:
        import aws_sdk_pinpoint.types.segment_condition

        out["segment_condition"] = (
            aws_sdk_pinpoint.types.segment_condition.deserialize_json(
                data["SegmentCondition"]
            )
        )
    if "segmentDimensions" in data:
        import aws_sdk_pinpoint.types.segment_dimensions

        out["segment_dimensions"] = (
            aws_sdk_pinpoint.types.segment_dimensions.deserialize_json(
                data["segmentDimensions"]
            )
        )
    return out
