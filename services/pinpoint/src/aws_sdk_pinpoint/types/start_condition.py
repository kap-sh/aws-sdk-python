"""Generated from Smithy shape ``com.amazonaws.pinpoint#StartCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.event_start_condition
    import aws_sdk_pinpoint.types.segment_condition


class StartCondition(TypedDict, closed=True):
    description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The custom description of the condition.</p>"""
    event_start_condition: NotRequired[
        "aws_sdk_pinpoint.types.event_start_condition.EventStartCondition"
    ]
    segment_start_condition: NotRequired[
        "aws_sdk_pinpoint.types.segment_condition.SegmentCondition"
    ]
    """<p>The segment that's associated with the first activity in the journey. This segment determines which users are participants in the journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCondition) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "event_start_condition" in value:
        import aws_sdk_pinpoint.types.event_start_condition

        out["EventStartCondition"] = (
            aws_sdk_pinpoint.types.event_start_condition.serialize_json(
                value["event_start_condition"]
            )
        )
    if "segment_start_condition" in value:
        import aws_sdk_pinpoint.types.segment_condition

        out["SegmentStartCondition"] = (
            aws_sdk_pinpoint.types.segment_condition.serialize_json(
                value["segment_start_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartCondition:
    out: StartCondition = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventStartCondition" in data:
        import aws_sdk_pinpoint.types.event_start_condition

        out["event_start_condition"] = (
            aws_sdk_pinpoint.types.event_start_condition.deserialize_json(
                data["EventStartCondition"]
            )
        )
    if "SegmentStartCondition" in data:
        import aws_sdk_pinpoint.types.segment_condition

        out["segment_start_condition"] = (
            aws_sdk_pinpoint.types.segment_condition.deserialize_json(
                data["SegmentStartCondition"]
            )
        )
    return out
