"""Generated from Smithy shape ``com.amazonaws.ec2#GetSecurityGroupsForVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_for_vpc_list
    import aws_sdk_ec2.types.string


class GetSecurityGroupsForVpcResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    security_group_for_vpcs: NotRequired[
        "aws_sdk_ec2.types.security_group_for_vpc_list.SecurityGroupForVpcList"
    ]
    """<p>The security group that can be used by interfaces in the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetSecurityGroupsForVpcResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "security_group_for_vpcs" in value:
        import aws_sdk_ec2.types.security_group_for_vpc_list

        aws_sdk_ec2.types.security_group_for_vpc_list.serialize_ec2_query(
            value["security_group_for_vpcs"], pairs, f"{prefix}.SecurityGroupForVpcSet"
        )


def deserialize_ec2_query(el: Element) -> GetSecurityGroupsForVpcResult:
    out: GetSecurityGroupsForVpcResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("SecurityGroupForVpcSet") is not None:
        import aws_sdk_ec2.types.security_group_for_vpc_list

        out["security_group_for_vpcs"] = (
            aws_sdk_ec2.types.security_group_for_vpc_list.deserialize_ec2_query(
                el, "SecurityGroupForVpcSet"
            )
        )
    return out
