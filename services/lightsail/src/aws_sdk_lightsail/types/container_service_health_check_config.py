"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceHealthCheckConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.string


class ContainerServiceHealthCheckConfig(TypedDict):
    healthy_threshold: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The number of consecutive health checks successes required before moving the container to the <code>Healthy</code> state. The default value is <code>2</code>.</p>"""
    unhealthy_threshold: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The number of consecutive health check failures required before moving the container to the <code>Unhealthy</code> state. The default value is <code>2</code>.</p>"""
    timeout_seconds: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is <code>2</code>.</p>"""
    interval_seconds: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is <code>5</code>.</p>"""
    path: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The path on the container on which to perform the health check. The default value is <code>/</code>.</p>"""
    success_codes: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The HTTP codes to use when checking for a successful response from a container. You can specify values between <code>200</code> and <code>499</code>. You can specify multiple values (for example, <code>200,202</code>) or a range of values (for example, <code>200-299</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceHealthCheckConfig) -> dict:
    out: dict = {}
    if "healthy_threshold" in value:
        out["healthyThreshold"] = value["healthy_threshold"]
    if "unhealthy_threshold" in value:
        out["unhealthyThreshold"] = value["unhealthy_threshold"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "interval_seconds" in value:
        out["intervalSeconds"] = value["interval_seconds"]
    if "path" in value:
        out["path"] = value["path"]
    if "success_codes" in value:
        out["successCodes"] = value["success_codes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceHealthCheckConfig:
    out: ContainerServiceHealthCheckConfig = {}  # type: ignore[typeddict-item]
    if "healthyThreshold" in data:
        out["healthy_threshold"] = data["healthyThreshold"]
    if "unhealthyThreshold" in data:
        out["unhealthy_threshold"] = data["unhealthyThreshold"]
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if "intervalSeconds" in data:
        out["interval_seconds"] = data["intervalSeconds"]
    if "path" in data:
        out["path"] = data["path"]
    if "successCodes" in data:
        out["success_codes"] = data["successCodes"]
    return out
