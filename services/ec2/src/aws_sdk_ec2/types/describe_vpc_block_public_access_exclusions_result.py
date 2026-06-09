"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcBlockPublicAccessExclusionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_list


class DescribeVpcBlockPublicAccessExclusionsResult(TypedDict):
    vpc_block_public_access_exclusions: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_list.VpcBlockPublicAccessExclusionList"
    ]
    """<p>Details related to the exclusions.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcBlockPublicAccessExclusionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_block_public_access_exclusions" in value:
        import aws_sdk_ec2.types.vpc_block_public_access_exclusion_list

        aws_sdk_ec2.types.vpc_block_public_access_exclusion_list.serialize_ec2_query(
            value["vpc_block_public_access_exclusions"],
            pairs,
            f"{prefix}.VpcBlockPublicAccessExclusionSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcBlockPublicAccessExclusionsResult:
    out: DescribeVpcBlockPublicAccessExclusionsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcBlockPublicAccessExclusionSet") is not None:
        import aws_sdk_ec2.types.vpc_block_public_access_exclusion_list

        out["vpc_block_public_access_exclusions"] = (
            aws_sdk_ec2.types.vpc_block_public_access_exclusion_list.deserialize_ec2_query(
                el, "VpcBlockPublicAccessExclusionSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
