"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashBaseUrl``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError


class DashBaseUrl(TypedDict):
    url: "str"
    """<p>A source location for segments.</p>"""
    service_location: NotRequired["str"]
    """<p>The name of the source location.</p>"""
    dvb_priority: NotRequired["int"]
    """<p>For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.</p>"""
    dvb_weight: NotRequired["int"]
    """<p>For use with DVB-DASH profiles only. The weighting for source locations that have the same priority. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashBaseUrl) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    if "service_location" in value:
        out["ServiceLocation"] = value["service_location"]
    if "dvb_priority" in value:
        out["DvbPriority"] = value["dvb_priority"]
    if "dvb_weight" in value:
        out["DvbWeight"] = value["dvb_weight"]
    return out


def deserialize_json(data: dict) -> DashBaseUrl:
    out: DashBaseUrl = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("DashBaseUrl.url required")
    if "ServiceLocation" in data:
        out["service_location"] = data["ServiceLocation"]
    if "DvbPriority" in data:
        out["dvb_priority"] = data["DvbPriority"]
    if "DvbWeight" in data:
        out["dvb_weight"] = data["DvbWeight"]
    return out
