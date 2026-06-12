"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyLimits``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.journey_timeframe_cap


class JourneyLimits(TypedDict):
    daily_cap: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages that the journey can send to a single participant during a 24-hour period. The maximum value is 100.</p>"""
    endpoint_reentry_cap: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of times that a participant can enter the journey. The maximum value is 100. To allow participants to enter the journey an unlimited number of times, set this value to 0.</p>"""
    messages_per_second: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages that the journey can send each second.</p>"""
    endpoint_reentry_interval: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Minimum time that must pass before an endpoint can re-enter a given journey. The duration should use an ISO 8601 format, such as PT1H. </p>"""
    timeframe_cap: NotRequired[
        "aws_sdk_pinpoint.types.journey_timeframe_cap.JourneyTimeframeCap"
    ]
    """<p>The number of messages that an endpoint can receive during the specified timeframe.</p>"""
    total_cap: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of messages a journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyLimits) -> dict:
    out: dict = {}
    if "daily_cap" in value:
        out["DailyCap"] = value["daily_cap"]
    if "endpoint_reentry_cap" in value:
        out["EndpointReentryCap"] = value["endpoint_reentry_cap"]
    if "messages_per_second" in value:
        out["MessagesPerSecond"] = value["messages_per_second"]
    if "endpoint_reentry_interval" in value:
        out["EndpointReentryInterval"] = value["endpoint_reentry_interval"]
    if "timeframe_cap" in value:
        import aws_sdk_pinpoint.types.journey_timeframe_cap

        out["TimeframeCap"] = (
            aws_sdk_pinpoint.types.journey_timeframe_cap.serialize_json(
                value["timeframe_cap"]
            )
        )
    if "total_cap" in value:
        out["TotalCap"] = value["total_cap"]
    return out


def deserialize_json(data: dict) -> JourneyLimits:
    out: JourneyLimits = {}  # type: ignore[typeddict-item]
    if "DailyCap" in data:
        out["daily_cap"] = data["DailyCap"]
    if "EndpointReentryCap" in data:
        out["endpoint_reentry_cap"] = data["EndpointReentryCap"]
    if "MessagesPerSecond" in data:
        out["messages_per_second"] = data["MessagesPerSecond"]
    if "EndpointReentryInterval" in data:
        out["endpoint_reentry_interval"] = data["EndpointReentryInterval"]
    if "TimeframeCap" in data:
        import aws_sdk_pinpoint.types.journey_timeframe_cap

        out["timeframe_cap"] = (
            aws_sdk_pinpoint.types.journey_timeframe_cap.deserialize_json(
                data["TimeframeCap"]
            )
        )
    if "TotalCap" in data:
        out["total_cap"] = data["TotalCap"]
    return out
