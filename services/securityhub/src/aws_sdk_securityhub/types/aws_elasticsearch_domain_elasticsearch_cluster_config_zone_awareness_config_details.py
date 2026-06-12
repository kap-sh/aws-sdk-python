"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails(
    TypedDict
):
    availability_zone_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>he number of Availability Zones that the domain uses. Valid values are 2 and 3. The default is 2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails,
) -> dict:
    out: dict = {}
    if "availability_zone_count" in value:
        out["AvailabilityZoneCount"] = value["availability_zone_count"]
    return out


def deserialize_json(
    data: dict,
) -> AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails:
    out: AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails = {}  # type: ignore[typeddict-item]
    if "AvailabilityZoneCount" in data:
        out["availability_zone_count"] = data["AvailabilityZoneCount"]
    return out
