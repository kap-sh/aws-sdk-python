"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPolicyAllocationRulesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_document


class ModifyIpamPolicyAllocationRulesResult(TypedDict):
    ipam_policy_document: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_document.IpamPolicyDocument"
    ]
    """<p>The modified IPAM policy containing the updated allocation rules.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPolicyAllocationRulesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_policy_document" in value:
        import aws_sdk_ec2.types.ipam_policy_document

        aws_sdk_ec2.types.ipam_policy_document.serialize_ec2_query(
            value["ipam_policy_document"], pairs, f"{prefix}.IpamPolicyDocument"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamPolicyAllocationRulesResult:
    out: ModifyIpamPolicyAllocationRulesResult = {}  # type: ignore[typeddict-item]
    child_ipam_policy_document = el.find("IpamPolicyDocument")
    if child_ipam_policy_document is not None:
        import aws_sdk_ec2.types.ipam_policy_document

        out["ipam_policy_document"] = (
            aws_sdk_ec2.types.ipam_policy_document.deserialize_ec2_query(
                child_ipam_policy_document
            )
        )
    return out
