"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string


class GetResourcePolicyRequest(TypedDict):
    resource_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
