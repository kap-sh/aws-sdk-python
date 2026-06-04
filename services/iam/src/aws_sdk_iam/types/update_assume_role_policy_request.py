"""Generated from Smithy shape ``com.amazonaws.iam#UpdateAssumeRolePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_document_type
    import aws_sdk_iam.types.role_name_type


class UpdateAssumeRolePolicyRequest(TypedDict):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    """<p>The name of the role to update with the new policy.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    policy_document: "aws_sdk_iam.types.policy_document_type.policyDocumentType"
    """<p>The policy that grants an entity permission to assume the role.</p> <p>You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00ff</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000a</code>), and carriage return (<code>\u000d</code>)</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateAssumeRolePolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))
    pairs.append((f"{prefix}.PolicyDocument", str(value["policy_document"])))


def deserialize_query(el: Element) -> UpdateAssumeRolePolicyRequest:
    out: UpdateAssumeRolePolicyRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("UpdateAssumeRolePolicyRequest.role_name required")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    else:
        raise DeserializationError(
            "UpdateAssumeRolePolicyRequest.policy_document required"
        )
    return out
