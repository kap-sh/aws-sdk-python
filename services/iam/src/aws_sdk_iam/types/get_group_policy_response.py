"""Generated from Smithy shape ``com.amazonaws.iam#GetGroupPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.group_name_type
    import aws_sdk_iam.types.policy_document_type
    import aws_sdk_iam.types.policy_name_type


class GetGroupPolicyResponse(TypedDict):
    group_name: "aws_sdk_iam.types.group_name_type.groupNameType"
    """<p>The group the policy is associated with.</p>"""
    policy_name: "aws_sdk_iam.types.policy_name_type.policyNameType"
    """<p>The name of the policy.</p>"""
    policy_document: "aws_sdk_iam.types.policy_document_type.policyDocumentType"
    """<p>The policy document.</p> <p>IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetGroupPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    pairs.append((f"{prefix}.PolicyDocument", str(value["policy_document"])))


def deserialize_query(el: Element) -> GetGroupPolicyResponse:
    out: GetGroupPolicyResponse = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("GetGroupPolicyResponse.group_name required")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("GetGroupPolicyResponse.policy_name required")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    else:
        raise DeserializationError("GetGroupPolicyResponse.policy_document required")
    return out
