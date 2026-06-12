"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.port


class TargetFailure(TypedDict):
    id: NotRequired["str"]
    """<p>The ID of the target. If the target group type is <code>INSTANCE</code>, this is an instance ID. If the target group type is <code>IP</code>, this is an IP address. If the target group type is <code>LAMBDA</code>, this is the ARN of a Lambda function. If the target group type is <code>ALB</code>, this is the ARN of an Application Load Balancer.</p>"""
    port: NotRequired["aws_sdk_vpc_lattice.types.port.Port"]
    """<p>The port on which the target is listening. This parameter doesn't apply if the target is a Lambda function.</p>"""
    failure_code: NotRequired["str"]
    """<p>The failure code.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetFailure) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "port" in value:
        out["port"] = value["port"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> TargetFailure:
    out: TargetFailure = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "port" in data:
        out["port"] = data["port"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
