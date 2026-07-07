"""Generated from Smithy shape ``com.amazonaws.ec2#Region``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.region_geography_list
    import aws_sdk_ec2.types.string


class Region(TypedDict, closed=True):
    opt_in_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region opt-in status. The possible values are <code>opt-in-not-required</code>, <code>opted-in</code>, and <code>not-opted-in</code>.</p>"""
    geography: NotRequired[
        "aws_sdk_ec2.types.region_geography_list.RegionGeographyList"
    ]
    """<p>The geography information for the Region. The geography is returned as a list.</p>"""
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Region.</p>"""
    endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region service endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Region, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "opt_in_status" in value:
        pairs.append((f"{prefix}.OptInStatus", str(value["opt_in_status"])))
    if "geography" in value:
        import aws_sdk_ec2.types.region_geography_list

        aws_sdk_ec2.types.region_geography_list.serialize_ec2_query(
            value["geography"], pairs, f"{prefix}.GeographySet"
        )
    if "region_name" in value:
        pairs.append((f"{prefix}.RegionName", str(value["region_name"])))
    if "endpoint" in value:
        pairs.append((f"{prefix}.RegionEndpoint", str(value["endpoint"])))


def deserialize_ec2_query(el: Element) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    child_opt_in_status = el.find("OptInStatus")
    if child_opt_in_status is not None:
        out["opt_in_status"] = str(child_opt_in_status.text or "")
    if el.find("GeographySet") is not None:
        import aws_sdk_ec2.types.region_geography_list

        out["geography"] = (
            aws_sdk_ec2.types.region_geography_list.deserialize_ec2_query(
                el, "GeographySet"
            )
        )
    child_region_name = el.find("RegionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    child_endpoint = el.find("RegionEndpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    return out
