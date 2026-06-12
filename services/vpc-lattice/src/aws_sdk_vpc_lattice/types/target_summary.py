"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.port
    import aws_sdk_vpc_lattice.types.target_status


class TargetSummary(TypedDict):
    id: NotRequired["str"]
    """<p>The ID of the target. If the target group type is <code>INSTANCE</code>, this is an instance ID. If the target group type is <code>IP</code>, this is an IP address. If the target group type is <code>LAMBDA</code>, this is the ARN of a Lambda function. If the target type is <code>ALB</code>, this is the ARN of an Application Load Balancer.</p>"""
    port: NotRequired["aws_sdk_vpc_lattice.types.port.Port"]
    """<p>The port on which the target is listening.</p>"""
    status: NotRequired["aws_sdk_vpc_lattice.types.target_status.TargetStatus"]
    """<p>The status of the target.</p> <ul> <li> <p> <code>DRAINING</code>: The target is being deregistered. No new connections are sent to this target while current connections are being drained. The default draining time is 1 minute.</p> </li> <li> <p> <code>UNAVAILABLE</code>: Health checks are unavailable for the target group.</p> </li> <li> <p> <code>HEALTHY</code>: The target is healthy.</p> </li> <li> <p> <code>UNHEALTHY</code>: The target is unhealthy.</p> </li> <li> <p> <code>INITIAL</code>: Initial health checks on the target are being performed.</p> </li> <li> <p> <code>UNUSED</code>: Target group is not used in a service.</p> </li> </ul>"""
    reason_code: NotRequired["str"]
    """<p>The code for why the target status is what it is.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "port" in value:
        out["port"] = value["port"]
    if "status" in value:
        out["status"] = value["status"]
    if "reason_code" in value:
        out["reasonCode"] = value["reason_code"]
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "port" in data:
        out["port"] = data["port"]
    if "status" in data:
        out["status"] = data["status"]
    if "reasonCode" in data:
        out["reason_code"] = data["reasonCode"]
    return out
