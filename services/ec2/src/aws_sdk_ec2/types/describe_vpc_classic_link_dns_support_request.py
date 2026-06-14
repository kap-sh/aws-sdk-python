"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkDnsSupportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_max_results
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token
    import aws_sdk_ec2.types.vpc_classic_link_id_list


class DescribeVpcClassicLinkDnsSupportRequest(TypedDict):
    vpc_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_classic_link_id_list.VpcClassicLinkIdList"
    ]
    """<p>The IDs of the VPCs.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_max_results.DescribeVpcClassicLinkDnsSupportMaxResults"
    ]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired[
        "aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token.DescribeVpcClassicLinkDnsSupportNextToken"
    ]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcClassicLinkDnsSupportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_ids" in value:
        import aws_sdk_ec2.types.vpc_classic_link_id_list

        aws_sdk_ec2.types.vpc_classic_link_id_list.serialize_ec2_query(
            value["vpc_ids"], pairs, f"{prefix}.VpcIds"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcClassicLinkDnsSupportRequest:
    out: DescribeVpcClassicLinkDnsSupportRequest = {}  # type: ignore[typeddict-item]
    if el.find("VpcIds") is not None:
        import aws_sdk_ec2.types.vpc_classic_link_id_list

        out["vpc_ids"] = (
            aws_sdk_ec2.types.vpc_classic_link_id_list.deserialize_ec2_query(
                el, "VpcIds"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
