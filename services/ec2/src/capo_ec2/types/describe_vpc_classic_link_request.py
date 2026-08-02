"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.vpc_classic_link_id_list


class DescribeVpcClassicLinkRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_ids: NotRequired["capo_ec2.types.vpc_classic_link_id_list.VpcClassicLinkIdList"]
    """<p>The VPCs for which you want to describe the ClassicLink status.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>is-classic-link-enabled</code> - Whether the VPC is enabled for ClassicLink (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcClassicLinkRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_ids" in value:
        import capo_ec2.types.vpc_classic_link_id_list

        capo_ec2.types.vpc_classic_link_id_list.serialize_ec2_query(
            value["vpc_ids"], pairs, f"{key_prefix}VpcIds"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcClassicLinkRequest:
    out: DescribeVpcClassicLinkRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("VpcIds") is not None:
        import capo_ec2.types.vpc_classic_link_id_list

        out["vpc_ids"] = capo_ec2.types.vpc_classic_link_id_list.deserialize_ec2_query(
            el, "VpcIds"
        )
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    return out
