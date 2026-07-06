"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#UpdateRoutingControlStateEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53_recovery_cluster.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_cluster.types.arn
    import aws_sdk_route53_recovery_cluster.types.routing_control_state


class UpdateRoutingControlStateEntry(TypedDict, closed=True):
    routing_control_arn: "aws_sdk_route53_recovery_cluster.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a routing control state entry.</p>"""
    routing_control_state: "aws_sdk_route53_recovery_cluster.types.routing_control_state.RoutingControlState"
    """<p>The routing control state in a set of routing control state entries.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRoutingControlStateEntry) -> dict:
    out: dict = {}
    out["RoutingControlArn"] = value["routing_control_arn"]
    import aws_sdk_route53_recovery_cluster.types.routing_control_state

    out["RoutingControlState"] = (
        aws_sdk_route53_recovery_cluster.types.routing_control_state.serialize_aws_json_1_0(
            value["routing_control_state"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRoutingControlStateEntry:
    out: UpdateRoutingControlStateEntry = {}  # type: ignore[typeddict-item]
    if "RoutingControlArn" in data:
        out["routing_control_arn"] = data["RoutingControlArn"]
    else:
        raise DeserializationError(
            "UpdateRoutingControlStateEntry.routing_control_arn required"
        )
    if "RoutingControlState" in data:
        import aws_sdk_route53_recovery_cluster.types.routing_control_state

        out["routing_control_state"] = (
            aws_sdk_route53_recovery_cluster.types.routing_control_state.deserialize_aws_json_1_0(
                data["RoutingControlState"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingControlStateEntry.routing_control_state required"
        )
    return out
