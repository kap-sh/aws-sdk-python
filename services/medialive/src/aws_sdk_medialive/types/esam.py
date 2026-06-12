"""Generated from Smithy shape ``com.amazonaws.medialive#Esam``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min_negative1000_max1000
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_max256
    import aws_sdk_medialive.types.__string_max2048


class Esam(TypedDict):
    acquisition_point_id: NotRequired[
        "aws_sdk_medialive.types.__string_max256.__stringMax256"
    ]
    """Sent as acquisitionPointIdentity to identify the MediaLive channel to the POIS."""
    ad_avail_offset: NotRequired[
        "aws_sdk_medialive.types.__integer_min_negative1000_max1000.__integerMinNegative1000Max1000"
    ]
    """When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages."""
    password_param: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Documentation update needed"""
    pois_endpoint: NotRequired[
        "aws_sdk_medialive.types.__string_max2048.__stringMax2048"
    ]
    """The URL of the signal conditioner endpoint on the Placement Opportunity Information System (POIS). MediaLive sends SignalProcessingEvents here when SCTE-35 messages are read."""
    username: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Documentation update needed"""
    zone_identity: NotRequired["aws_sdk_medialive.types.__string_max256.__stringMax256"]
    """Optional data sent as zoneIdentity to identify the MediaLive channel to the POIS."""


# --- restJson1 ser/de ---
def serialize_json(value: Esam) -> dict:
    out: dict = {}
    if "acquisition_point_id" in value:
        out["acquisitionPointId"] = value["acquisition_point_id"]
    if "ad_avail_offset" in value:
        out["adAvailOffset"] = value["ad_avail_offset"]
    if "password_param" in value:
        out["passwordParam"] = value["password_param"]
    if "pois_endpoint" in value:
        out["poisEndpoint"] = value["pois_endpoint"]
    if "username" in value:
        out["username"] = value["username"]
    if "zone_identity" in value:
        out["zoneIdentity"] = value["zone_identity"]
    return out


def deserialize_json(data: dict) -> Esam:
    out: Esam = {}  # type: ignore[typeddict-item]
    if "acquisitionPointId" in data:
        out["acquisition_point_id"] = data["acquisitionPointId"]
    if "adAvailOffset" in data:
        out["ad_avail_offset"] = data["adAvailOffset"]
    if "passwordParam" in data:
        out["password_param"] = data["passwordParam"]
    if "poisEndpoint" in data:
        out["pois_endpoint"] = data["poisEndpoint"]
    if "username" in data:
        out["username"] = data["username"]
    if "zoneIdentity" in data:
        out["zone_identity"] = data["zoneIdentity"]
    return out
