"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_group_summary

KeyGroupSummaryList: TypeAlias = list[
    "capo_cloudfront.types.key_group_summary.KeyGroupSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: KeyGroupSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.key_group_summary

        capo_cloudfront.types.key_group_summary.serialize_xml(
            item, el, "KeyGroupSummary"
        )


def deserialize_xml(el: Element) -> KeyGroupSummaryList:
    import capo_cloudfront.types.key_group_summary

    out: KeyGroupSummaryList = []
    for child in el.findall("KeyGroupSummary"):
        out.append(capo_cloudfront.types.key_group_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: KeyGroupSummaryList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.key_group_summary

        capo_cloudfront.types.key_group_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> KeyGroupSummaryList:
    import capo_cloudfront.types.key_group_summary

    out: KeyGroupSummaryList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.key_group_summary.deserialize_xml(child))
    return out
