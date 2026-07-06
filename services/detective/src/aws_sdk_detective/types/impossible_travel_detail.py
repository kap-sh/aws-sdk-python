"""Generated from Smithy shape ``com.amazonaws.detective#ImpossibleTravelDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.hourly_time_delta
    import aws_sdk_detective.types.ip_address
    import aws_sdk_detective.types.location


class ImpossibleTravelDetail(TypedDict, closed=True):
    starting_ip_address: NotRequired["aws_sdk_detective.types.ip_address.IpAddress"]
    """<p>IP address where the resource was first used in the impossible travel.</p>"""
    ending_ip_address: NotRequired["aws_sdk_detective.types.ip_address.IpAddress"]
    """<p>IP address where the resource was last used in the impossible travel.</p>"""
    starting_location: NotRequired["aws_sdk_detective.types.location.Location"]
    """<p>Location where the resource was first used in the impossible travel.</p>"""
    ending_location: NotRequired["aws_sdk_detective.types.location.Location"]
    """<p>Location where the resource was last used in the impossible travel.</p>"""
    hourly_time_delta: NotRequired[
        "aws_sdk_detective.types.hourly_time_delta.HourlyTimeDelta"
    ]
    """<p>Returns the time difference between the first and last timestamp the resource was used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpossibleTravelDetail) -> dict:
    out: dict = {}
    if "starting_ip_address" in value:
        out["StartingIpAddress"] = value["starting_ip_address"]
    if "ending_ip_address" in value:
        out["EndingIpAddress"] = value["ending_ip_address"]
    if "starting_location" in value:
        out["StartingLocation"] = value["starting_location"]
    if "ending_location" in value:
        out["EndingLocation"] = value["ending_location"]
    if "hourly_time_delta" in value:
        out["HourlyTimeDelta"] = value["hourly_time_delta"]
    return out


def deserialize_json(data: dict) -> ImpossibleTravelDetail:
    out: ImpossibleTravelDetail = {}  # type: ignore[typeddict-item]
    if "StartingIpAddress" in data:
        out["starting_ip_address"] = data["StartingIpAddress"]
    if "EndingIpAddress" in data:
        out["ending_ip_address"] = data["EndingIpAddress"]
    if "StartingLocation" in data:
        out["starting_location"] = data["StartingLocation"]
    if "EndingLocation" in data:
        out["ending_location"] = data["EndingLocation"]
    if "HourlyTimeDelta" in data:
        out["hourly_time_delta"] = data["HourlyTimeDelta"]
    return out
