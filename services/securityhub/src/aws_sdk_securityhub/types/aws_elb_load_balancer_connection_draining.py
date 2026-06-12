"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerConnectionDraining``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer


class AwsElbLoadBalancerConnectionDraining(TypedDict):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether connection draining is enabled for the load balancer.</p>"""
    timeout: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The maximum time, in seconds, to keep the existing connections open before deregistering the instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerConnectionDraining) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerConnectionDraining:
    out: AwsElbLoadBalancerConnectionDraining = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    return out
