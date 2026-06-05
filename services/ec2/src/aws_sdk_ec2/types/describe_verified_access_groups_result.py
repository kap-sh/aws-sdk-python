"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_group_list


class DescribeVerifiedAccessGroupsResult(TypedDict):
    verified_access_groups: NotRequired[
        "aws_sdk_ec2.types.verified_access_group_list.VerifiedAccessGroupList"
    ]
    """<p>Details about the Verified Access groups.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_groups" in value:
        import aws_sdk_ec2.types.verified_access_group_list

        aws_sdk_ec2.types.verified_access_group_list.serialize_ec2_query(
            value["verified_access_groups"], pairs, f"{prefix}.VerifiedAccessGroupSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessGroupsResult:
    out: DescribeVerifiedAccessGroupsResult = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessGroupSet") is not None:
        import aws_sdk_ec2.types.verified_access_group_list

        out["verified_access_groups"] = (
            aws_sdk_ec2.types.verified_access_group_list.deserialize_ec2_query(
                el, "VerifiedAccessGroupSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
