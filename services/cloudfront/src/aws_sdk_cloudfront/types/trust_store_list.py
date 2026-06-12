"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustStoreList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.trust_store_summary

TrustStoreList: TypeAlias = list[
    "aws_sdk_cloudfront.types.trust_store_summary.TrustStoreSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: TrustStoreList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.trust_store_summary

        aws_sdk_cloudfront.types.trust_store_summary.serialize_xml(
            item, el, "TrustStoreSummary"
        )


def deserialize_xml(el: Element) -> TrustStoreList:
    import aws_sdk_cloudfront.types.trust_store_summary

    out: TrustStoreList = []
    for child in el.findall("TrustStoreSummary"):
        out.append(aws_sdk_cloudfront.types.trust_store_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TrustStoreList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.trust_store_summary

        aws_sdk_cloudfront.types.trust_store_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TrustStoreList:
    import aws_sdk_cloudfront.types.trust_store_summary

    out: TrustStoreList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.trust_store_summary.deserialize_xml(child))
    return out
