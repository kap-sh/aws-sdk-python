"""Generated from Smithy shape ``com.amazonaws.pinpoint#ApplicationSettingsJourneyLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.journey_timeframe_cap


class ApplicationSettingsJourneyLimits(TypedDict, closed=True):
    daily_cap: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The daily number of messages that an endpoint can receive from all journeys. The maximum value is 100. If set to 0, this limit will not apply.</p>"""
    timeframe_cap: NotRequired[
        "capo_pinpoint.types.journey_timeframe_cap.JourneyTimeframeCap"
    ]
    """<p>The default maximum number of messages that can be sent to an endpoint during the specified timeframe for all journeys.</p>"""
    total_cap: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The default maximum number of messages that a single journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSettingsJourneyLimits) -> dict:
    out: dict = {}
    if "daily_cap" in value:
        out["DailyCap"] = value["daily_cap"]
    if "timeframe_cap" in value:
        import capo_pinpoint.types.journey_timeframe_cap

        out["TimeframeCap"] = capo_pinpoint.types.journey_timeframe_cap.serialize_json(
            value["timeframe_cap"]
        )
    if "total_cap" in value:
        out["TotalCap"] = value["total_cap"]
    return out


def deserialize_json(data: dict) -> ApplicationSettingsJourneyLimits:
    out: ApplicationSettingsJourneyLimits = {}  # type: ignore[typeddict-item]
    if "DailyCap" in data:
        out["daily_cap"] = data["DailyCap"]
    if "TimeframeCap" in data:
        import capo_pinpoint.types.journey_timeframe_cap

        out["timeframe_cap"] = (
            capo_pinpoint.types.journey_timeframe_cap.deserialize_json(
                data["TimeframeCap"]
            )
        )
    if "TotalCap" in data:
        out["total_cap"] = data["TotalCap"]
    return out
