"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventDimensions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.map_of_attribute_dimension
    import aws_sdk_pinpoint.types.map_of_metric_dimension
    import aws_sdk_pinpoint.types.set_dimension


class EventDimensions(TypedDict):
    attributes: NotRequired[
        "aws_sdk_pinpoint.types.map_of_attribute_dimension.MapOfAttributeDimension"
    ]
    """<p>One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.</p>"""
    event_type: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as _email.delivered. For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html\">Streaming Amazon Pinpoint Events</a> in the <i>Amazon Pinpoint Developer Guide</i>.</p>"""
    metrics: NotRequired[
        "aws_sdk_pinpoint.types.map_of_metric_dimension.MapOfMetricDimension"
    ]
    """<p>One or more custom metrics that your application reports to Amazon Pinpoint. You can use these metrics as selection criteria when you create an event filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDimensions) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_pinpoint.types.map_of_attribute_dimension

        out["Attributes"] = (
            aws_sdk_pinpoint.types.map_of_attribute_dimension.serialize_json(
                value["attributes"]
            )
        )
    if "event_type" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["EventType"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["event_type"]
        )
    if "metrics" in value:
        import aws_sdk_pinpoint.types.map_of_metric_dimension

        out["Metrics"] = aws_sdk_pinpoint.types.map_of_metric_dimension.serialize_json(
            value["metrics"]
        )
    return out


def deserialize_json(data: dict) -> EventDimensions:
    out: EventDimensions = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_pinpoint.types.map_of_attribute_dimension

        out["attributes"] = (
            aws_sdk_pinpoint.types.map_of_attribute_dimension.deserialize_json(
                data["Attributes"]
            )
        )
    if "EventType" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["event_type"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["EventType"]
        )
    if "Metrics" in data:
        import aws_sdk_pinpoint.types.map_of_metric_dimension

        out["metrics"] = (
            aws_sdk_pinpoint.types.map_of_metric_dimension.deserialize_json(
                data["Metrics"]
            )
        )
    return out
