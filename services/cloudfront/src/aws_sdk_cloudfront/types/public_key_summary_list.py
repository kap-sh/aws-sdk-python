"""Generated from Smithy shape ``com.amazonaws.cloudfront#PublicKeySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.public_key_summary

PublicKeySummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.public_key_summary.PublicKeySummary"
]


# --- restXml ser/de ---
def serialize_xml(value: PublicKeySummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.public_key_summary

        aws_sdk_cloudfront.types.public_key_summary.serialize_xml(
            item, el, "PublicKeySummary"
        )


def deserialize_xml(el: Element) -> PublicKeySummaryList:
    import aws_sdk_cloudfront.types.public_key_summary

    out: PublicKeySummaryList = []
    for child in el.findall("PublicKeySummary"):
        out.append(aws_sdk_cloudfront.types.public_key_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: PublicKeySummaryList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.public_key_summary

        aws_sdk_cloudfront.types.public_key_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> PublicKeySummaryList:
    import aws_sdk_cloudfront.types.public_key_summary

    out: PublicKeySummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.public_key_summary.deserialize_xml(child))
    return out
