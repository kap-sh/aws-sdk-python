"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateRoutingControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09


class UpdateRoutingControlRequest(TypedDict, closed=True):
    routing_control_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the routing control.</p>"""
    routing_control_name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the routing control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingControlRequest) -> dict:
    out: dict = {}
    if "routing_control_arn" in value:
        out["RoutingControlArn"] = value["routing_control_arn"]
    if "routing_control_name" in value:
        out["RoutingControlName"] = value["routing_control_name"]
    return out


def deserialize_json(data: dict) -> UpdateRoutingControlRequest:
    out: UpdateRoutingControlRequest = {}  # type: ignore[typeddict-item]
    if "RoutingControlArn" in data:
        out["routing_control_arn"] = data["RoutingControlArn"]
    if "RoutingControlName" in data:
        out["routing_control_name"] = data["RoutingControlName"]
    return out
