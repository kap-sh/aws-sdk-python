"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyAllocationRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_document_set
    import capo_ec2.types.next_token


class GetIpamPolicyAllocationRulesResult(TypedDict, closed=True):
    ipam_policy_documents: NotRequired[
        "capo_ec2.types.ipam_policy_document_set.IpamPolicyDocumentSet"
    ]
    """<p>The IPAM policy documents containing the allocation rules.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPolicyAllocationRulesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_policy_documents" in value:
        import capo_ec2.types.ipam_policy_document_set

        capo_ec2.types.ipam_policy_document_set.serialize_ec2_query(
            value["ipam_policy_documents"], pairs, f"{key_prefix}IpamPolicyDocumentSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPolicyAllocationRulesResult:
    out: GetIpamPolicyAllocationRulesResult = {}  # type: ignore[typeddict-item]
    if el.find("ipamPolicyDocumentSet") is not None:
        import capo_ec2.types.ipam_policy_document_set

        out["ipam_policy_documents"] = (
            capo_ec2.types.ipam_policy_document_set.deserialize_ec2_query(
                el, "ipamPolicyDocumentSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
