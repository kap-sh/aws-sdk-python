"""Generated from Smithy shape ``com.amazonaws.ses#PutIdentityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity
    import aws_sdk_ses.types.policy
    import aws_sdk_ses.types.policy_name


class PutIdentityPolicyRequest(TypedDict, closed=True):
    identity: "aws_sdk_ses.types.identity.Identity"
    """<p>The identity to which that the policy applies. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>"""
    policy_name: "aws_sdk_ses.types.policy_name.PolicyName"
    """<p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>"""
    policy: "aws_sdk_ses.types.policy.Policy"
    r"""<p>The text of the policy in JSON format. The policy cannot exceed 4 KB.</p> <p>For information about the syntax of sending authorization policies, see the <a href=\"https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-policies.html\">Amazon SES Developer Guide</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutIdentityPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Identity", str(value["identity"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    pairs.append((f"{prefix}.Policy", str(value["policy"])))


def deserialize_query(el: Element) -> PutIdentityPolicyRequest:
    out: PutIdentityPolicyRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError("PutIdentityPolicyRequest.identity required")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("PutIdentityPolicyRequest.policy_name required")
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    else:
        raise DeserializationError("PutIdentityPolicyRequest.policy required")
    return out
