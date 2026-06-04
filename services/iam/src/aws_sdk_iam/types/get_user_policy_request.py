"""Generated from Smithy shape ``com.amazonaws.iam#GetUserPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.existing_user_name_type
    import aws_sdk_iam.types.policy_name_type


class GetUserPolicyRequest(TypedDict):
    user_name: "aws_sdk_iam.types.existing_user_name_type.existingUserNameType"
    """<p>The name of the user who the policy is associated with.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    policy_name: "aws_sdk_iam.types.policy_name_type.policyNameType"
    """<p>The name of the policy document to get.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetUserPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))


def deserialize_query(el: Element) -> GetUserPolicyRequest:
    out: GetUserPolicyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("GetUserPolicyRequest.user_name required")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("GetUserPolicyRequest.policy_name required")
    return out
