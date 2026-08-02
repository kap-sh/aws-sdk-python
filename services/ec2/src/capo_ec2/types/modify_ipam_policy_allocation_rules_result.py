"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPolicyAllocationRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_document


class ModifyIpamPolicyAllocationRulesResult(TypedDict, closed=True):
    ipam_policy_document: NotRequired[
        "capo_ec2.types.ipam_policy_document.IpamPolicyDocument"
    ]
    """<p>The modified IPAM policy containing the updated allocation rules.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPolicyAllocationRulesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_policy_document" in value:
        import capo_ec2.types.ipam_policy_document

        capo_ec2.types.ipam_policy_document.serialize_ec2_query(
            value["ipam_policy_document"], pairs, f"{key_prefix}IpamPolicyDocument"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamPolicyAllocationRulesResult:
    out: ModifyIpamPolicyAllocationRulesResult = {}  # type: ignore[typeddict-item]
    child_ipam_policy_document = el.find("IpamPolicyDocument")
    if child_ipam_policy_document is not None:
        import capo_ec2.types.ipam_policy_document

        out["ipam_policy_document"] = (
            capo_ec2.types.ipam_policy_document.deserialize_ec2_query(
                child_ipam_policy_document
            )
        )
    return out
