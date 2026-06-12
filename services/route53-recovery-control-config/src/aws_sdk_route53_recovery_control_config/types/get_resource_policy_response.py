"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__policy


class GetResourcePolicyResponse(TypedDict):
    policy: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__policy.__policy"
    ]
    """<p>The resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
