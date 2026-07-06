"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.open_hours
    import aws_sdk_connectcampaignsv2.types.restricted_periods


class TimeWindow(TypedDict, closed=True):
    open_hours: "aws_sdk_connectcampaignsv2.types.open_hours.OpenHours"
    restricted_periods: NotRequired[
        "aws_sdk_connectcampaignsv2.types.restricted_periods.RestrictedPeriods"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TimeWindow) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.open_hours

    out["openHours"] = aws_sdk_connectcampaignsv2.types.open_hours.serialize_json(
        value["open_hours"]
    )
    if "restricted_periods" in value:
        import aws_sdk_connectcampaignsv2.types.restricted_periods

        out["restrictedPeriods"] = (
            aws_sdk_connectcampaignsv2.types.restricted_periods.serialize_json(
                value["restricted_periods"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimeWindow:
    out: TimeWindow = {}  # type: ignore[typeddict-item]
    if "openHours" in data:
        import aws_sdk_connectcampaignsv2.types.open_hours

        out["open_hours"] = (
            aws_sdk_connectcampaignsv2.types.open_hours.deserialize_json(
                data["openHours"]
            )
        )
    else:
        raise DeserializationError("TimeWindow.open_hours required")
    if "restrictedPeriods" in data:
        import aws_sdk_connectcampaignsv2.types.restricted_periods

        out["restricted_periods"] = (
            aws_sdk_connectcampaignsv2.types.restricted_periods.deserialize_json(
                data["restrictedPeriods"]
            )
        )
    return out
