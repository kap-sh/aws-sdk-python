"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_list
    import aws_sdk_ec2.types.string


class DescribeSecurityGroupsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.security_group_list.SecurityGroupList"
    ]
    """<p>Information about the security groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "security_groups" in value:
        import aws_sdk_ec2.types.security_group_list

        aws_sdk_ec2.types.security_group_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroupInfo"
        )


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupsResult:
    out: DescribeSecurityGroupsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("SecurityGroupInfo") is not None:
        import aws_sdk_ec2.types.security_group_list

        out["security_groups"] = (
            aws_sdk_ec2.types.security_group_list.deserialize_ec2_query(
                el, "SecurityGroupInfo"
            )
        )
    return out
