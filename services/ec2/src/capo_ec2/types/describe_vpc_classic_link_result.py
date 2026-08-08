"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_classic_link_list


class DescribeVpcClassicLinkResult(TypedDict, closed=True):
    vpcs: NotRequired["capo_ec2.types.vpc_classic_link_list.VpcClassicLinkList"]
    """<p>The ClassicLink status of the VPCs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcClassicLinkResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpcs" in value:
        import capo_ec2.types.vpc_classic_link_list

        capo_ec2.types.vpc_classic_link_list.serialize_ec2_query(
            value["vpcs"], pairs, f"{key_prefix}VpcSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcClassicLinkResult:
    out: DescribeVpcClassicLinkResult = {}  # type: ignore[typeddict-item]
    if el.find("vpcSet") is not None:
        import capo_ec2.types.vpc_classic_link_list

        out["vpcs"] = capo_ec2.types.vpc_classic_link_list.deserialize_ec2_query(
            el, "vpcSet"
        )
    return out
