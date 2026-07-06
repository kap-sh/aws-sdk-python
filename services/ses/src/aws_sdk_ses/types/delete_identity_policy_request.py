"""Generated from Smithy shape ``com.amazonaws.ses#DeleteIdentityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity
    import aws_sdk_ses.types.policy_name


class DeleteIdentityPolicyRequest(TypedDict, closed=True):
    identity: "aws_sdk_ses.types.identity.Identity"
    """<p>The identity that is associated with the policy to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>"""
    policy_name: "aws_sdk_ses.types.policy_name.PolicyName"
    """<p>The name of the policy to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIdentityPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Identity", str(value["identity"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))


def deserialize_query(el: Element) -> DeleteIdentityPolicyRequest:
    out: DeleteIdentityPolicyRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError("DeleteIdentityPolicyRequest.identity required")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("DeleteIdentityPolicyRequest.policy_name required")
    return out
