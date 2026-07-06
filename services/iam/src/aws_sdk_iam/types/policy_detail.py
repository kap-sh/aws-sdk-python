"""Generated from Smithy shape ``com.amazonaws.iam#PolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_document_type
    import aws_sdk_iam.types.policy_name_type


class PolicyDetail(TypedDict, closed=True):
    policy_name: NotRequired["aws_sdk_iam.types.policy_name_type.policyNameType"]
    """<p>The name of the policy.</p>"""
    policy_document: NotRequired[
        "aws_sdk_iam.types.policy_document_type.policyDocumentType"
    ]
    """<p>The policy document.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "policy_document" in value:
        pairs.append((f"{prefix}.PolicyDocument", str(value["policy_document"])))


def deserialize_query(el: Element) -> PolicyDetail:
    out: PolicyDetail = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    return out
