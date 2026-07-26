"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DeleteRoutingControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string


class DeleteRoutingControlRequest(TypedDict, closed=True):
    routing_control_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the routing control that you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoutingControlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoutingControlRequest:
    out: DeleteRoutingControlRequest = {}  # type: ignore[typeddict-item]
    return out
