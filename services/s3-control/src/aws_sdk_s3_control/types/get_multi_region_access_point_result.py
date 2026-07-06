"""Generated from Smithy shape ``com.amazonaws.s3control#GetMultiRegionAccessPointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.multi_region_access_point_report


class GetMultiRegionAccessPointResult(TypedDict, closed=True):
    access_point: NotRequired[
        "aws_sdk_s3_control.types.multi_region_access_point_report.MultiRegionAccessPointReport"
    ]
    """<p>A container element containing the details of the requested Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMultiRegionAccessPointResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "access_point" in value:
        import aws_sdk_s3_control.types.multi_region_access_point_report

        aws_sdk_s3_control.types.multi_region_access_point_report.serialize_xml(
            value["access_point"], el, "AccessPoint"
        )


def deserialize_xml(el: Element) -> GetMultiRegionAccessPointResult:
    out: GetMultiRegionAccessPointResult = {}  # type: ignore[typeddict-item]
    child_access_point = el.find("AccessPoint")
    if child_access_point is not None:
        import aws_sdk_s3_control.types.multi_region_access_point_report

        out["access_point"] = (
            aws_sdk_s3_control.types.multi_region_access_point_report.deserialize_xml(
                child_access_point
            )
        )
    return out
