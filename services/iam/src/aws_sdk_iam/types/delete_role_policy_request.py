"""Generated from Smithy shape ``com.amazonaws.iam#DeleteRolePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_name_type
    import aws_sdk_iam.types.role_name_type


class DeleteRolePolicyRequest(TypedDict, closed=True):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    r"""<p>The name (friendly name, not ARN) identifying the role that the policy is embedded in.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    policy_name: "aws_sdk_iam.types.policy_name_type.policyNameType"
    r"""<p>The name of the inline policy to delete from the specified IAM role.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteRolePolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))


def deserialize_query(el: Element) -> DeleteRolePolicyRequest:
    out: DeleteRolePolicyRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("DeleteRolePolicyRequest.role_name required")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("DeleteRolePolicyRequest.policy_name required")
    return out
