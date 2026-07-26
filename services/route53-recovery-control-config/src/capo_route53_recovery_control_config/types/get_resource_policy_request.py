"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
