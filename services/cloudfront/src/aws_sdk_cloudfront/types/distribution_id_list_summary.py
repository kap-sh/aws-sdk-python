"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionIdListSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string

DistributionIdListSummary: TypeAlias = list["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: DistributionIdListSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "DistributionId").text = str(item)


def deserialize_xml(el: Element) -> DistributionIdListSummary:
    out: DistributionIdListSummary = []
    for child in el.findall("DistributionId"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(
    value: DistributionIdListSummary, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> DistributionIdListSummary:
    out: DistributionIdListSummary = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
