"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity
    import aws_sdk_ses.types.policy_name_list


class GetIdentityPoliciesRequest(TypedDict, closed=True):
    identity: "aws_sdk_ses.types.identity.Identity"
    """<p>The identity for which the policies are retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: <code>user@example.com</code>, <code>example.com</code>, <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> <p>To successfully call this operation, you must own the identity.</p>"""
    policy_names: "aws_sdk_ses.types.policy_name_list.PolicyNameList"
    """<p>A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use <code>ListIdentityPolicies</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityPoliciesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Identity", str(value["identity"])))
    import aws_sdk_ses.types.policy_name_list

    aws_sdk_ses.types.policy_name_list.serialize_query(
        value["policy_names"], pairs, f"{prefix}.PolicyNames"
    )


def deserialize_query(el: Element) -> GetIdentityPoliciesRequest:
    out: GetIdentityPoliciesRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError("GetIdentityPoliciesRequest.identity required")
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import aws_sdk_ses.types.policy_name_list

        out["policy_names"] = aws_sdk_ses.types.policy_name_list.deserialize_query(
            child_policy_names
        )
    else:
        raise DeserializationError("GetIdentityPoliciesRequest.policy_names required")
    return out
