"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyAllocationRulesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_document_set
    import aws_sdk_ec2.types.next_token


class GetIpamPolicyAllocationRulesResult(TypedDict):
    ipam_policy_documents: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_document_set.IpamPolicyDocumentSet"
    ]
    """<p>The IPAM policy documents containing the allocation rules.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPolicyAllocationRulesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_policy_documents" in value:
        import aws_sdk_ec2.types.ipam_policy_document_set

        aws_sdk_ec2.types.ipam_policy_document_set.serialize_ec2_query(
            value["ipam_policy_documents"], pairs, f"{prefix}.IpamPolicyDocumentSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPolicyAllocationRulesResult:
    out: GetIpamPolicyAllocationRulesResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamPolicyDocumentSet") is not None:
        import aws_sdk_ec2.types.ipam_policy_document_set

        out["ipam_policy_documents"] = (
            aws_sdk_ec2.types.ipam_policy_document_set.deserialize_ec2_query(
                el, "IpamPolicyDocumentSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
