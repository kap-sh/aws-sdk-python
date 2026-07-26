"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerCrossZoneLoadBalancing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsElbLoadBalancerCrossZoneLoadBalancing(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
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
