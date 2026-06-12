"""Generated from Smithy shape ``com.amazonaws.location#ForecastGeofenceEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_location.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_location.types.distance_unit
    import aws_sdk_location.types.forecasted_events_list
    import aws_sdk_location.types.large_token
    import aws_sdk_location.types.speed_unit

class ForecastGeofenceEventsResponse(TypedDict):
    forecasted_events: "aws_sdk_location.types.forecasted_events_list.ForecastedEventsList"
    """<p>The list of forecasted events.</p>"""
    next_token: NotRequired["aws_sdk_location.types.large_token.LargeToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""
    distance_unit: "aws_sdk_location.types.distance_unit.DistanceUnit"
    """<p>The distance unit for the forecasted events.</p>"""
    speed_unit: "aws_sdk_location.types.speed_unit.SpeedUnit"
    """<p>The speed unit for the forecasted events.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ForecastGeofenceEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.forecasted_events_list
    out["ForecastedEvents"] = aws_sdk_location.types.forecasted_events_list.serialize_json(value["forecasted_events"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["DistanceUnit"] = value["distance_unit"]
    out["SpeedUnit"] = value["speed_unit"]
    return out


def deserialize_json(data: dict) -> ForecastGeofenceEventsResponse:
    out: ForecastGeofenceEventsResponse = {}  # type: ignore[typeddict-item]
    if "ForecastedEvents" in data:
        import aws_sdk_location.types.forecasted_events_list
        out["forecasted_events"] = aws_sdk_location.types.forecasted_events_list.deserialize_json(data["ForecastedEvents"])
    else:
        raise DeserializationError("ForecastGeofenceEventsResponse.forecasted_events required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DistanceUnit" in data:
        out["distance_unit"] = data["DistanceUnit"]
    else:
        raise DeserializationError("ForecastGeofenceEventsResponse.distance_unit required")
    if "SpeedUnit" in data:
        out["speed_unit"] = data["SpeedUnit"]
    else:
        raise DeserializationError("ForecastGeofenceEventsResponse.speed_unit required")
    return out