"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteEmailIdentityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.identity
    import aws_sdk_sesv2.types.policy_name


class DeleteEmailIdentityPolicyRequest(TypedDict, closed=True):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    policy_name: "aws_sdk_sesv2.types.policy_name.PolicyName"
    """<p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailIdentityPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailIdentityPolicyRequest:
    out: DeleteEmailIdentityPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
