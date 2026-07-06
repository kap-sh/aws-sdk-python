"""Generated from Smithy shape ``com.amazonaws.iam#DeleteGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.group_name_type
    import aws_sdk_iam.types.policy_name_type


class DeleteGroupPolicyRequest(TypedDict, closed=True):
    group_name: "aws_sdk_iam.types.group_name_type.groupNameType"
    r"""<p>The name (friendly name, not ARN) identifying the group that the policy is embedded in.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    policy_name: "aws_sdk_iam.types.policy_name_type.policyNameType"
    r"""<p>The name identifying the policy document to delete.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteGroupPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))


def deserialize_query(el: Element) -> DeleteGroupPolicyRequest:
    out: DeleteGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("DeleteGroupPolicyRequest.group_name required")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("DeleteGroupPolicyRequest.policy_name required")
    return out
