"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#GetRoutingControlStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53_recovery_cluster.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn


class GetRoutingControlStateRequest(TypedDict, closed=True):
    routing_control_arn: "capo_route53_recovery_cluster.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the routing control that you want to get the state for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRoutingControlStateRequest) -> dict:
    out: dict = {}
    out["RoutingControlArn"] = value["routing_control_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRoutingControlStateRequest:
    out: GetRoutingControlStateRequest = {}  # type: ignore[typeddict-item]
    if "RoutingControlArn" in data:
        out["routing_control_arn"] = data["RoutingControlArn"]
    else:
        raise DeserializationError(
            "GetRoutingControlStateRequest.routing_control_arn required"
        )
    return out
