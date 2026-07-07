"""Generated from Smithy shape ``com.amazonaws.personalizeevents#MetricAttribution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.event_attribution_source


class MetricAttribution(TypedDict, closed=True):
    event_attribution_source: "aws_sdk_personalize_events.types.event_attribution_source.EventAttributionSource"
    """<p>The source of the event, such as a third party.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricAttribution) -> dict:
    out: dict = {}
    out["eventAttributionSource"] = value["event_attribution_source"]
    return out


def deserialize_json(data: dict) -> MetricAttribution:
    out: MetricAttribution = {}  # type: ignore[typeddict-item]
    if "eventAttributionSource" in data:
        out["event_attribution_source"] = data["eventAttributionSource"]
    else:
        raise DeserializationError(
            "MetricAttribution.event_attribution_source required"
        )
    return out
