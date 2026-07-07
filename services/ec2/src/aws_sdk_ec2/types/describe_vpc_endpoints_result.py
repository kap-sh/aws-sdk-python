"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_set


class DescribeVpcEndpointsResult(TypedDict, closed=True):
    vpc_endpoints: NotRequired["aws_sdk_ec2.types.vpc_endpoint_set.VpcEndpointSet"]
    """<p>Information about the VPC endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_endpoints" in value:
        import aws_sdk_ec2.types.vpc_endpoint_set

        aws_sdk_ec2.types.vpc_endpoint_set.serialize_ec2_query(
            value["vpc_endpoints"], pairs, f"{prefix}.VpcEndpointSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointsResult:
    out: DescribeVpcEndpointsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcEndpointSet") is not None:
        import aws_sdk_ec2.types.vpc_endpoint_set

        out["vpc_endpoints"] = aws_sdk_ec2.types.vpc_endpoint_set.deserialize_ec2_query(
            el, "VpcEndpointSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
