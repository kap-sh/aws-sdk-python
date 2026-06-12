"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#RestrictedPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.iso8601_date
    import aws_sdk_connectcampaignsv2.types.restricted_period_name


class RestrictedPeriod(TypedDict):
    name: NotRequired[
        "aws_sdk_connectcampaignsv2.types.restricted_period_name.RestrictedPeriodName"
    ]
    start_date: "aws_sdk_connectcampaignsv2.types.iso8601_date.Iso8601Date"
    end_date: "aws_sdk_connectcampaignsv2.types.iso8601_date.Iso8601Date"


# --- restJson1 ser/de ---
def serialize_json(value: RestrictedPeriod) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["startDate"] = value["start_date"]
    out["endDate"] = value["end_date"]
    return out


def deserialize_json(data: dict) -> RestrictedPeriod:
    out: RestrictedPeriod = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "startDate" in data:
        out["start_date"] = data["startDate"]
    else:
        raise DeserializationError("RestrictedPeriod.start_date required")
    if "endDate" in data:
        out["end_date"] = data["endDate"]
    else:
        raise DeserializationError("RestrictedPeriod.end_date required")
    return out
