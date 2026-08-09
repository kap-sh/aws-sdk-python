"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.verified_access_group_list


class DescribeVerifiedAccessGroupsResult(TypedDict, closed=True):
    verified_access_groups: NotRequired[
        "capo_ec2.types.verified_access_group_list.VerifiedAccessGroupList"
    ]
    """<p>Details about the Verified Access groups.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_groups" in value:
        import capo_ec2.types.verified_access_group_list

        capo_ec2.types.verified_access_group_list.serialize_ec2_query(
            value["verified_access_groups"],
            pairs,
            f"{key_prefix}VerifiedAccessGroupSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessGroupsResult:
    out: DescribeVerifiedAccessGroupsResult = {}  # type: ignore[typeddict-item]
    child_verified_access_groups = el.find("verifiedAccessGroupSet")
    if child_verified_access_groups is not None:
        import capo_ec2.types.verified_access_group_list

        out["verified_access_groups"] = (
            capo_ec2.types.verified_access_group_list.deserialize_ec2_query(
                child_verified_access_groups
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
