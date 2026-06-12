"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginCustomHeadersList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_custom_header

OriginCustomHeadersList: TypeAlias = list[
    "aws_sdk_cloudfront.types.origin_custom_header.OriginCustomHeader"
]


# --- restXml ser/de ---
def serialize_xml(value: OriginCustomHeadersList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.origin_custom_header

        aws_sdk_cloudfront.types.origin_custom_header.serialize_xml(
            item, el, "OriginCustomHeader"
        )


def deserialize_xml(el: Element) -> OriginCustomHeadersList:
    import aws_sdk_cloudfront.types.origin_custom_header

    out: OriginCustomHeadersList = []
    for child in el.findall("OriginCustomHeader"):
        out.append(aws_sdk_cloudfront.types.origin_custom_header.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: OriginCustomHeadersList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.origin_custom_header

        aws_sdk_cloudfront.types.origin_custom_header.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> OriginCustomHeadersList:
    import aws_sdk_cloudfront.types.origin_custom_header

    out: OriginCustomHeadersList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.origin_custom_header.deserialize_xml(child))
    return out
