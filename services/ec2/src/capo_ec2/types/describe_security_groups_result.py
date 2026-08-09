"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_list
    import capo_ec2.types.string


class DescribeSecurityGroupsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    security_groups: NotRequired["capo_ec2.types.security_group_list.SecurityGroupList"]
    """<p>Information about the security groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecurityGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "security_groups" in value:
        import capo_ec2.types.security_group_list

        capo_ec2.types.security_group_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroupInfo"
        )


def deserialize_ec2_query(el: Element) -> DescribeSecurityGroupsResult:
    out: DescribeSecurityGroupsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_security_groups = el.find("securityGroupInfo")
    if child_security_groups is not None:
        import capo_ec2.types.security_group_list

        out["security_groups"] = (
            capo_ec2.types.security_group_list.deserialize_ec2_query(
                child_security_groups
            )
        )
    return out
