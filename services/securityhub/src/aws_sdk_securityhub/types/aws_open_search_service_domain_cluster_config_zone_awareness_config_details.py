"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails(TypedDict):
    availability_zone_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of Availability Zones that the domain uses. Valid values are <code>2</code> or <code>3</code>. The default is <code>2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails,
) -> dict:
    out: dict = {}
    if "availability_zone_count" in value:
        out["AvailabilityZoneCount"] = value["availability_zone_count"]
    return out


def deserialize_json(
    data: dict,
) -> AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails:
    out: AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails = {}  # type: ignore[typeddict-item]
    if "AvailabilityZoneCount" in data:
        out["availability_zone_count"] = data["AvailabilityZoneCount"]
    return out
