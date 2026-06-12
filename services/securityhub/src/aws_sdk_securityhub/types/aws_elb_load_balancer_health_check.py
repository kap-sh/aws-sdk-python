"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerHealthCheck``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbLoadBalancerHealthCheck(TypedDict):
    healthy_threshold: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of consecutive health check successes required before the instance is moved to the Healthy state.</p>"""
    interval: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The approximate interval, in seconds, between health checks of an individual instance.</p>"""
    target: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The instance that is being checked. The target specifies the protocol and port. The available protocols are TCP, SSL, HTTP, and HTTPS. The range of valid ports is 1 through 65535.</p> <p>For the HTTP and HTTPS protocols, the target also specifies the ping path.</p> <p>For the TCP protocol, the target is specified as <code>TCP: <i><port></i> </code>.</p> <p>For the SSL protocol, the target is specified as <code>SSL.<i><port></i> </code>.</p> <p>For the HTTP and HTTPS protocols, the target is specified as <code> <i><protocol></i>:<i><port></i>/<i><path to ping></i> </code>.</p>"""
    timeout: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The amount of time, in seconds, during which no response means a failed health check.</p>"""
    unhealthy_threshold: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of consecutive health check failures that must occur before the instance is moved to the Unhealthy state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerHealthCheck) -> dict:
    out: dict = {}
    if "healthy_threshold" in value:
        out["HealthyThreshold"] = value["healthy_threshold"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "target" in value:
        out["Target"] = value["target"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "unhealthy_threshold" in value:
        out["UnhealthyThreshold"] = value["unhealthy_threshold"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerHealthCheck:
    out: AwsElbLoadBalancerHealthCheck = {}  # type: ignore[typeddict-item]
    if "HealthyThreshold" in data:
        out["healthy_threshold"] = data["HealthyThreshold"]
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "UnhealthyThreshold" in data:
        out["unhealthy_threshold"] = data["UnhealthyThreshold"]
    return out
