"""Generated from Smithy shape ``com.amazonaws.opensearch#ZoneAwarenessConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.integer_class


class ZoneAwarenessConfig(TypedDict):
    availability_zone_count: NotRequired[
        "aws_sdk_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>If you enabled multiple Availability Zones, this value is the number of zones that you want the domain to use. Valid values are <code>2</code> and <code>3</code>. If your domain is provisioned within a VPC, this value be equal to number of subnets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZoneAwarenessConfig) -> dict:
    out: dict = {}
    if "availability_zone_count" in value:
        out["AvailabilityZoneCount"] = value["availability_zone_count"]
    return out


def deserialize_json(data: dict) -> ZoneAwarenessConfig:
    out: ZoneAwarenessConfig = {}  # type: ignore[typeddict-item]
    if "AvailabilityZoneCount" in data:
        out["availability_zone_count"] = data["AvailabilityZoneCount"]
    return out
