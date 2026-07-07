"""Generated from Smithy shape ``com.amazonaws.securityhub#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AvailabilityZone(TypedDict, closed=True):
    zone_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Availability Zone.</p>"""
    subnet_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the subnet. You can specify one subnet per Availability Zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZone) -> dict:
    out: dict = {}
    if "zone_name" in value:
        out["ZoneName"] = value["zone_name"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    if "ZoneName" in data:
        out["zone_name"] = data["ZoneName"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    return out
