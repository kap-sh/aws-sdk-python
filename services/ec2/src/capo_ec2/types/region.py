"""Generated from Smithy shape ``com.amazonaws.ec2#Region``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.region_geography_list
    import capo_ec2.types.string


class Region(TypedDict, closed=True):
    opt_in_status: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region opt-in status. The possible values are <code>opt-in-not-required</code>, <code>opted-in</code>, and <code>not-opted-in</code>.</p>"""
    geography: NotRequired["capo_ec2.types.region_geography_list.RegionGeographyList"]
    """<p>The geography information for the Region. The geography is returned as a list.</p>"""
    region_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Region.</p>"""
    endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region service endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Region, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "opt_in_status" in value:
        pairs.append((f"{key_prefix}OptInStatus", str(value["opt_in_status"])))
    if "geography" in value:
        import capo_ec2.types.region_geography_list

        capo_ec2.types.region_geography_list.serialize_ec2_query(
            value["geography"], pairs, f"{key_prefix}GeographySet"
        )
    if "region_name" in value:
        pairs.append((f"{key_prefix}RegionName", str(value["region_name"])))
    if "endpoint" in value:
        pairs.append((f"{key_prefix}RegionEndpoint", str(value["endpoint"])))


def deserialize_ec2_query(el: Element) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    child_opt_in_status = el.find("optInStatus")
    if child_opt_in_status is not None:
        out["opt_in_status"] = str(child_opt_in_status.text or "")
    child_geography = el.find("geographySet")
    if child_geography is not None:
        import capo_ec2.types.region_geography_list

        out["geography"] = capo_ec2.types.region_geography_list.deserialize_ec2_query(
            child_geography
        )
    child_region_name = el.find("regionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    child_endpoint = el.find("regionEndpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    return out
