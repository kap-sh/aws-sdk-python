"""Generated from Smithy shape ``com.amazonaws.xray#AvailabilityZoneDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.string


class AvailabilityZoneDetail(TypedDict):
    name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The name of a corresponding Availability Zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AvailabilityZoneDetail:
    out: AvailabilityZoneDetail = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
