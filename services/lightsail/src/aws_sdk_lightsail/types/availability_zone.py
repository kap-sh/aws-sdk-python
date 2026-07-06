"""Generated from Smithy shape ``com.amazonaws.lightsail#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.non_empty_string


class AvailabilityZone(TypedDict, closed=True):
    zone_name: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Availability Zone. The format is <code>us-east-2a</code> (case-sensitive).</p>"""
    state: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The state of the Availability Zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZone) -> dict:
    out: dict = {}
    if "zone_name" in value:
        out["zoneName"] = value["zone_name"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    if "zoneName" in data:
        out["zone_name"] = data["zoneName"]
    if "state" in data:
        out["state"] = data["state"]
    return out
