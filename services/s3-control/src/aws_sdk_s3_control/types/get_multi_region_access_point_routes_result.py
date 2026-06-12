"""Generated from Smithy shape ``com.amazonaws.s3control#GetMultiRegionAccessPointRoutesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.multi_region_access_point_id
    import aws_sdk_s3_control.types.route_list


class GetMultiRegionAccessPointRoutesResult(TypedDict):
    mrap: NotRequired[
        "aws_sdk_s3_control.types.multi_region_access_point_id.MultiRegionAccessPointId"
    ]
    """<p>The Multi-Region Access Point ARN.</p>"""
    routes: NotRequired["aws_sdk_s3_control.types.route_list.RouteList"]
    """<p>The different routes that make up the route configuration. Active routes return a value of <code>100</code>, and passive routes return a value of <code>0</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMultiRegionAccessPointRoutesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "mrap" in value:
        SubElement(el, "Mrap").text = str(value["mrap"])
    if "routes" in value:
        import aws_sdk_s3_control.types.route_list

        aws_sdk_s3_control.types.route_list.serialize_xml(value["routes"], el, "Routes")


def deserialize_xml(el: Element) -> GetMultiRegionAccessPointRoutesResult:
    out: GetMultiRegionAccessPointRoutesResult = {}  # type: ignore[typeddict-item]
    child_mrap = el.find("Mrap")
    if child_mrap is not None:
        out["mrap"] = str(child_mrap.text or "")
    child_routes = el.find("Routes")
    if child_routes is not None:
        import aws_sdk_s3_control.types.route_list

        out["routes"] = aws_sdk_s3_control.types.route_list.deserialize_xml(
            child_routes
        )
    return out
