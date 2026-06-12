"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#OpenHours``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.daily_hours


class _OpenHours_dailyHours(TypedDict):
    dailyHours: "aws_sdk_connectcampaignsv2.types.daily_hours.DailyHours"


OpenHours: TypeAlias = _OpenHours_dailyHours


# --- restJson1 ser/de ---
def serialize_json(value: OpenHours) -> dict:
    if "dailyHours" in value:
        import aws_sdk_connectcampaignsv2.types.daily_hours

        return {
            "dailyHours": aws_sdk_connectcampaignsv2.types.daily_hours.serialize_json(
                value["dailyHours"]
            )
        }
    else:
        raise SerializationError("OpenHours: no variant present")


def deserialize_json(data: dict) -> OpenHours:
    if "dailyHours" in data:
        import aws_sdk_connectcampaignsv2.types.daily_hours

        return {
            "dailyHours": aws_sdk_connectcampaignsv2.types.daily_hours.deserialize_json(
                data["dailyHours"]
            )
        }
    else:
        raise DeserializationError("OpenHours: no recognized variant key")
