"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointReportList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.multi_region_access_point_report

MultiRegionAccessPointReportList: TypeAlias = list[
    "aws_sdk_s3_control.types.multi_region_access_point_report.MultiRegionAccessPointReport"
]


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointReportList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.multi_region_access_point_report

        aws_sdk_s3_control.types.multi_region_access_point_report.serialize_xml(
            item, el, "AccessPoint"
        )


def deserialize_xml(el: Element) -> MultiRegionAccessPointReportList:
    import aws_sdk_s3_control.types.multi_region_access_point_report

    out: MultiRegionAccessPointReportList = []
    for child in el.findall("AccessPoint"):
        out.append(
            aws_sdk_s3_control.types.multi_region_access_point_report.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: MultiRegionAccessPointReportList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.multi_region_access_point_report

        aws_sdk_s3_control.types.multi_region_access_point_report.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> MultiRegionAccessPointReportList:
    import aws_sdk_s3_control.types.multi_region_access_point_report

    out: MultiRegionAccessPointReportList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.multi_region_access_point_report.deserialize_xml(
                child
            )
        )
    return out
