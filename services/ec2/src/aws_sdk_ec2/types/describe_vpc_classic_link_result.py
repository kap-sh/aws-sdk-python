"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_classic_link_list


class DescribeVpcClassicLinkResult(TypedDict):
    vpcs: NotRequired["aws_sdk_ec2.types.vpc_classic_link_list.VpcClassicLinkList"]
    """<p>The ClassicLink status of the VPCs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcClassicLinkResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpcs" in value:
        import aws_sdk_ec2.types.vpc_classic_link_list

        aws_sdk_ec2.types.vpc_classic_link_list.serialize_ec2_query(
            value["vpcs"], pairs, f"{prefix}.VpcSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcClassicLinkResult:
    out: DescribeVpcClassicLinkResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcSet") is not None:
        import aws_sdk_ec2.types.vpc_classic_link_list

        out["vpcs"] = aws_sdk_ec2.types.vpc_classic_link_list.deserialize_ec2_query(
            el, "VpcSet"
        )
    return out
