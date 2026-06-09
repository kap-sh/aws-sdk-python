"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_list


class DescribeVpcsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    vpcs: NotRequired["aws_sdk_ec2.types.vpc_list.VpcList"]
    """<p>Information about the VPCs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "vpcs" in value:
        import aws_sdk_ec2.types.vpc_list

        aws_sdk_ec2.types.vpc_list.serialize_ec2_query(
            value["vpcs"], pairs, f"{prefix}.VpcSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcsResult:
    out: DescribeVpcsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("VpcSet") is not None:
        import aws_sdk_ec2.types.vpc_list

        out["vpcs"] = aws_sdk_ec2.types.vpc_list.deserialize_ec2_query(el, "VpcSet")
    return out
