"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublicKeySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.public_key_summary

PublicKeySummaryList: TypeAlias = list[
    "capo_cloudfront.types.public_key_summary.PublicKeySummary"
]


# --- restXml ser/de ---
def serialize_xml(value: PublicKeySummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.public_key_summary

        capo_cloudfront.types.public_key_summary.serialize_xml(
            item, el, "PublicKeySummary"
        )


def deserialize_xml(el: Element) -> PublicKeySummaryList:
    import capo_cloudfront.types.public_key_summary

    out: PublicKeySummaryList = []
    for child in el.findall("PublicKeySummary"):
        out.append(capo_cloudfront.types.public_key_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: PublicKeySummaryList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.public_key_summary

        capo_cloudfront.types.public_key_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> PublicKeySummaryList:
    import capo_cloudfront.types.public_key_summary

    out: PublicKeySummaryList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.public_key_summary.deserialize_xml(child))
    return out
