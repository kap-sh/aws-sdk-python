"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DeleteRoutingControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string


class DeleteRoutingControlRequest(TypedDict):
    routing_control_arn: (
        "aws_sdk_route53_recovery_control_config.types.__string.__string"
    )
    """<p>The Amazon Resource Name (ARN) of the routing control that you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoutingControlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoutingControlRequest:
    out: DeleteRoutingControlRequest = {}  # type: ignore[typeddict-item]
    return out
