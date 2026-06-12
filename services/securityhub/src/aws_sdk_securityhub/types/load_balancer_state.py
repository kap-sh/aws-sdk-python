"""Generated from Smithy shape ``com.amazonaws.securityhub#LoadBalancerState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class LoadBalancerState(TypedDict):
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The state code. The initial state of the load balancer is provisioning.</p> <p>After the load balancer is fully set up and ready to route traffic, its state is active.</p> <p>If the load balancer could not be set up, its state is failed. </p>"""
    reason: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoadBalancerState) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> LoadBalancerState:
    out: LoadBalancerState = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
