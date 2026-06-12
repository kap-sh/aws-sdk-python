"""Generated from Smithy shape ``com.amazonaws.iot#DetachPrincipalPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name
    import aws_sdk_iot.types.principal


class DetachPrincipalPolicyRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The name of the policy to detach.</p>"""
    principal: "aws_sdk_iot.types.principal.Principal"
    """<p>The principal.</p> <p>Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>), thingGroupArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:thinggroup/<i>groupName</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachPrincipalPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DetachPrincipalPolicyRequest:
    out: DetachPrincipalPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
