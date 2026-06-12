"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ZoneAwarenessConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.integer_class


class ZoneAwarenessConfig(TypedDict):
    availability_zone_count: NotRequired[
        "aws_sdk_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p>An integer value to indicate the number of availability zones for a domain when zone awareness is enabled. This should be equal to number of subnets if VPC endpoints is enabled</p>"""


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
