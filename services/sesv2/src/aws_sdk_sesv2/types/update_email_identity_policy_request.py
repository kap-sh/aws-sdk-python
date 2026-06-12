"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateEmailIdentityPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.identity
    import aws_sdk_sesv2.types.policy
    import aws_sdk_sesv2.types.policy_name


class UpdateEmailIdentityPolicyRequest(TypedDict):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    policy_name: "aws_sdk_sesv2.types.policy_name.PolicyName"
    """<p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>"""
    policy: "aws_sdk_sesv2.types.policy.Policy"
    """<p>The text of the policy in JSON format. The policy cannot exceed 4 KB.</p> <p> For information about the syntax of sending authorization policies, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html\">Amazon SES Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEmailIdentityPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> UpdateEmailIdentityPolicyRequest:
    out: UpdateEmailIdentityPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("UpdateEmailIdentityPolicyRequest.policy required")
    return out
