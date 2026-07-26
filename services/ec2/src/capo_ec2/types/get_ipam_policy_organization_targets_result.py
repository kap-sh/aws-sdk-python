"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyOrganizationTargetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_organization_target_set
    import capo_ec2.types.next_token


class GetIpamPolicyOrganizationTargetsResult(TypedDict, closed=True):
    organization_targets: NotRequired[
        "capo_ec2.types.ipam_policy_organization_target_set.IpamPolicyOrganizationTargetSet"
    ]
    """<p>The IDs of the Amazon Web Services Organizations targets.</p> <p>A target can be an individual Amazon Web Services account or an entity within an Amazon Web Services Organization to which an IPAM policy can be applied.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPolicyOrganizationTargetsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "organization_targets" in value:
        import capo_ec2.types.ipam_policy_organization_target_set

        capo_ec2.types.ipam_policy_organization_target_set.serialize_ec2_query(
            value["organization_targets"], pairs, f"{prefix}.OrganizationTargetSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPolicyOrganizationTargetsResult:
    out: GetIpamPolicyOrganizationTargetsResult = {}  # type: ignore[typeddict-item]
    if el.find("OrganizationTargetSet") is not None:
        import capo_ec2.types.ipam_policy_organization_target_set

        out["organization_targets"] = (
            capo_ec2.types.ipam_policy_organization_target_set.deserialize_ec2_query(
                el, "OrganizationTargetSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
