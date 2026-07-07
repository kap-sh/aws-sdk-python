"""Generated from Smithy shape ``com.amazonaws.iot#AttachPrincipalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name
    import aws_sdk_iot.types.principal


class AttachPrincipalPolicyRequest(TypedDict, closed=True):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    principal: "aws_sdk_iot.types.principal.Principal"
    """<p>The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachPrincipalPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AttachPrincipalPolicyRequest:
    out: AttachPrincipalPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
