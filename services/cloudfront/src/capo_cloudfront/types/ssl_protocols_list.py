"""Generated from Smithy shape ``com.amazonaws.cloudfront#SslProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.ssl_protocol

SslProtocolsList: TypeAlias = list["capo_cloudfront.types.ssl_protocol.SslProtocol"]


# --- restXml ser/de ---
def serialize_xml(value: SslProtocolsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.ssl_protocol

        capo_cloudfront.types.ssl_protocol.serialize_xml(item, el, "SslProtocol")


def deserialize_xml(el: Element) -> SslProtocolsList:
    import capo_cloudfront.types.ssl_protocol

    out: SslProtocolsList = []
    for child in el.findall("SslProtocol"):
        out.append(capo_cloudfront.types.ssl_protocol.deserialize_xml(child))
    return out


def serialize_xml_flat(value: SslProtocolsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.ssl_protocol

        capo_cloudfront.types.ssl_protocol.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> SslProtocolsList:
    import capo_cloudfront.types.ssl_protocol

    out: SslProtocolsList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.ssl_protocol.deserialize_xml(child))
    return out
