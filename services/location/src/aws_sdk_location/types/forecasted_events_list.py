"""Generated from Smithy shape ``com.amazonaws.location#ForecastedEventsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.forecasted_event

ForecastedEventsList: TypeAlias = list["aws_sdk_location.types.forecasted_event.ForecastedEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: ForecastedEventsList) -> list:
    import aws_sdk_location.types.forecasted_event
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.forecasted_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ForecastedEventsList:
    import aws_sdk_location.types.forecasted_event
    out: ForecastedEventsList = []
    for item in data:
        out.append(aws_sdk_location.types.forecasted_event.deserialize_json(item))
    return out