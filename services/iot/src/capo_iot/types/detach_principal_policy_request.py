"""Generated from Smithy shape ``com.amazonaws.iot#DetachPrincipalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_name
    import capo_iot.types.principal


class DetachPrincipalPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The name of the policy to detach.</p>"""
    principal: "capo_iot.types.principal.Principal"
    """<p>The principal.</p> <p>Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>), thingGroupArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:thinggroup/<i>groupName</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachPrincipalPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DetachPrincipalPolicyRequest:
    out: DetachPrincipalPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
