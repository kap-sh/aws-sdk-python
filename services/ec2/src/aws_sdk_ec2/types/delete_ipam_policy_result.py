"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy


class DeleteIpamPolicyResult(TypedDict):
    ipam_policy: NotRequired["aws_sdk_ec2.types.ipam_policy.IpamPolicy"]
    """<p>Information about the deleted IPAM policy.</p> <p>An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_policy" in value:
        import aws_sdk_ec2.types.ipam_policy

        aws_sdk_ec2.types.ipam_policy.serialize_ec2_query(
            value["ipam_policy"], pairs, f"{prefix}.IpamPolicy"
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamPolicyResult:
    out: DeleteIpamPolicyResult = {}  # type: ignore[typeddict-item]
    child_ipam_policy = el.find("IpamPolicy")
    if child_ipam_policy is not None:
        import aws_sdk_ec2.types.ipam_policy

        out["ipam_policy"] = aws_sdk_ec2.types.ipam_policy.deserialize_ec2_query(
            child_ipam_policy
        )
    return out
