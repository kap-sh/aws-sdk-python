"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerCrossZoneLoadBalancing``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsElbLoadBalancerCrossZoneLoadBalancing(TypedDict):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether cross-zone load balancing is enabled for the load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerCrossZoneLoadBalancing) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerCrossZoneLoadBalancing:
    out: AwsElbLoadBalancerCrossZoneLoadBalancing = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
