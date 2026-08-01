"""Generated from Smithy shape ``com.amazonaws.cloudfront#AliasICPRecordals``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.alias_icp_recordal

AliasICPRecordals: TypeAlias = list[
    "capo_cloudfront.types.alias_icp_recordal.AliasICPRecordal"
]


# --- restXml ser/de ---
def serialize_xml(value: AliasICPRecordals, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.alias_icp_recordal

        capo_cloudfront.types.alias_icp_recordal.serialize_xml(
            item, el, "AliasICPRecordal"
        )


def deserialize_xml(el: Element) -> AliasICPRecordals:
    import capo_cloudfront.types.alias_icp_recordal

    out: AliasICPRecordals = []
    for child in el.findall("AliasICPRecordal"):
        out.append(capo_cloudfront.types.alias_icp_recordal.deserialize_xml(child))
    return out


def serialize_xml_flat(value: AliasICPRecordals, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.alias_icp_recordal

        capo_cloudfront.types.alias_icp_recordal.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> AliasICPRecordals:
    import capo_cloudfront.types.alias_icp_recordal

    out: AliasICPRecordals = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.alias_icp_recordal.deserialize_xml(child))
    return out
