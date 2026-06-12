"""Generated from Smithy shape ``com.amazonaws.iot#AttachPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name
    import aws_sdk_iot.types.policy_target


class AttachPolicyRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The name of the policy to attach.</p>"""
    target: "aws_sdk_iot.types.policy_target.PolicyTarget"
    """<p>The <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/security-iam.html\">identity</a> to which the policy is attached. For example, a thing group or a certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachPolicyRequest) -> dict:
    out: dict = {}
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> AttachPolicyRequest:
    out: AttachPolicyRequest = {}  # type: ignore[typeddict-item]
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError("AttachPolicyRequest.target required")
    return out
