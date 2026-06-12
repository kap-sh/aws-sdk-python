"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerConnectionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class AwsElbLoadBalancerConnectionSettings(TypedDict):
    idle_timeout: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The time, in seconds, that the connection can be idle (no data is sent over the connection) before it is closed by the load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerConnectionSettings) -> dict:
    out: dict = {}
    if "idle_timeout" in value:
        out["IdleTimeout"] = value["idle_timeout"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerConnectionSettings:
    out: AwsElbLoadBalancerConnectionSettings = {}  # type: ignore[typeddict-item]
    if "IdleTimeout" in data:
        out["idle_timeout"] = data["IdleTimeout"]
    return out
