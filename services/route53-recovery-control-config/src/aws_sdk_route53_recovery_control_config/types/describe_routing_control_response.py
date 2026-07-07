"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DescribeRoutingControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.routing_control


class DescribeRoutingControlResponse(TypedDict, closed=True):
    routing_control: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.routing_control.RoutingControl"
    ]
    """<p>Information about the routing control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoutingControlResponse) -> dict:
    out: dict = {}
    if "routing_control" in value:
        import aws_sdk_route53_recovery_control_config.types.routing_control

        out["RoutingControl"] = (
            aws_sdk_route53_recovery_control_config.types.routing_control.serialize_json(
                value["routing_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeRoutingControlResponse:
    out: DescribeRoutingControlResponse = {}  # type: ignore[typeddict-item]
    if "RoutingControl" in data:
        import aws_sdk_route53_recovery_control_config.types.routing_control

        out["routing_control"] = (
            aws_sdk_route53_recovery_control_config.types.routing_control.deserialize_json(
                data["RoutingControl"]
            )
        )
    return out
