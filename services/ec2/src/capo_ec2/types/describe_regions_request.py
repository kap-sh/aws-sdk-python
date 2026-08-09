"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRegionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.region_name_string_list


class DescribeRegionsRequest(TypedDict, closed=True):
    region_names: NotRequired[
        "capo_ec2.types.region_name_string_list.RegionNameStringList"
    ]
    """<p>The names of the Regions. You can specify any Regions, whether they are enabled and disabled for your account.</p>"""
    all_regions: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to display all Regions, including Regions that are disabled for your account.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>endpoint</code> - The endpoint of the Region (for example, <code>ec2.us-east-1.amazonaws.com</code>).</p> </li> <li> <p> <code>opt-in-status</code> - The opt-in status of the Region (<code>opt-in-not-required</code> | <code>opted-in</code> | <code>not-opted-in</code>).</p> </li> <li> <p> <code>region-name</code> - The name of the Region (for example, <code>us-east-1</code>).</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRegionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "region_names" in value:
        import capo_ec2.types.region_name_string_list

        capo_ec2.types.region_name_string_list.serialize_ec2_query(
            value["region_names"], pairs, f"{key_prefix}RegionName"
        )
    if "all_regions" in value:
        pairs.append(
            (f"{key_prefix}AllRegions", "true" if value["all_regions"] else "false")
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeRegionsRequest:
    out: DescribeRegionsRequest = {}  # type: ignore[typeddict-item]
    child_region_names = el.find("RegionName")
    if child_region_names is not None:
        import capo_ec2.types.region_name_string_list

        out["region_names"] = (
            capo_ec2.types.region_name_string_list.deserialize_ec2_query(
                child_region_names
            )
        )
    child_all_regions = el.find("AllRegions")
    if child_all_regions is not None:
        out["all_regions"] = (child_all_regions.text or "").lower() == "true"
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
