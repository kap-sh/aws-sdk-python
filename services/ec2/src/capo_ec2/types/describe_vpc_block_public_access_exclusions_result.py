"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcBlockPublicAccessExclusionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_block_public_access_exclusion_list


class DescribeVpcBlockPublicAccessExclusionsResult(TypedDict, closed=True):
    vpc_block_public_access_exclusions: NotRequired[
        "capo_ec2.types.vpc_block_public_access_exclusion_list.VpcBlockPublicAccessExclusionList"
    ]
    """<p>Details related to the exclusions.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcBlockPublicAccessExclusionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_block_public_access_exclusions" in value:
        import capo_ec2.types.vpc_block_public_access_exclusion_list

        capo_ec2.types.vpc_block_public_access_exclusion_list.serialize_ec2_query(
            value["vpc_block_public_access_exclusions"],
            pairs,
            f"{key_prefix}VpcBlockPublicAccessExclusionSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcBlockPublicAccessExclusionsResult:
    out: DescribeVpcBlockPublicAccessExclusionsResult = {}  # type: ignore[typeddict-item]
    if el.find("vpcBlockPublicAccessExclusionSet") is not None:
        import capo_ec2.types.vpc_block_public_access_exclusion_list

        out["vpc_block_public_access_exclusions"] = (
            capo_ec2.types.vpc_block_public_access_exclusion_list.deserialize_ec2_query(
                el, "vpcBlockPublicAccessExclusionSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
