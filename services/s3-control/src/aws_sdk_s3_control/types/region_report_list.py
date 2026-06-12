"""Generated from Smithy shape ``com.amazonaws.s3control#RegionReportList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.region_report

RegionReportList: TypeAlias = list[
    "aws_sdk_s3_control.types.region_report.RegionReport"
]


# --- restXml ser/de ---
def serialize_xml(value: RegionReportList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.region_report

        aws_sdk_s3_control.types.region_report.serialize_xml(item, el, "Region")


def deserialize_xml(el: Element) -> RegionReportList:
    import aws_sdk_s3_control.types.region_report

    out: RegionReportList = []
    for child in el.findall("Region"):
        out.append(aws_sdk_s3_control.types.region_report.deserialize_xml(child))
    return out


def serialize_xml_flat(value: RegionReportList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.region_report

        aws_sdk_s3_control.types.region_report.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> RegionReportList:
    import aws_sdk_s3_control.types.region_report

    out: RegionReportList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3_control.types.region_report.deserialize_xml(child))
    return out
