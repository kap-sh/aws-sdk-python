"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupVpcAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_vpc_association_list
    import capo_ec2.types.string


class DescribeSecurityGroupVpcAssociationsResult(TypedDict, closed=True):
    security_group_vpc_associations: NotRequired[
        "capo_ec2.types.security_group_vpc_association_list.SecurityGroupVpcAssociationList"
    ]
    """<p>The security group VPC associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupVpcAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "security_group_vpc_associations" in value:
        import capo_ec2.types.security_group_vpc_association_list

        capo_ec2.types.security_group_vpc_association_list.serialize_ec2_query(
            value["security_group_vpc_associations"],
            pairs,
            f"{key_prefix}SecurityGroupVpcAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupVpcAssociationsResult:
    out: DescribeSecurityGroupVpcAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("securityGroupVpcAssociationSet") is not None:
        import capo_ec2.types.security_group_vpc_association_list

        out["security_group_vpc_associations"] = (
            capo_ec2.types.security_group_vpc_association_list.deserialize_ec2_query(
                el, "securityGroupVpcAssociationSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
