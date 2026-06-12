"""Generated from Smithy shape ``com.amazonaws.cloudfront#SslProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.ssl_protocol

SslProtocolsList: TypeAlias = list["aws_sdk_cloudfront.types.ssl_protocol.SslProtocol"]


# --- restXml ser/de ---
def serialize_xml(value: SslProtocolsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.ssl_protocol

        aws_sdk_cloudfront.types.ssl_protocol.serialize_xml(item, el, "SslProtocol")


def deserialize_xml(el: Element) -> SslProtocolsList:
    import aws_sdk_cloudfront.types.ssl_protocol

    out: SslProtocolsList = []
    for child in el.findall("SslProtocol"):
        out.append(aws_sdk_cloudfront.types.ssl_protocol.deserialize_xml(child))
    return out


def serialize_xml_flat(value: SslProtocolsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.ssl_protocol

        aws_sdk_cloudfront.types.ssl_protocol.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> SslProtocolsList:
    import aws_sdk_cloudfront.types.ssl_protocol

    out: SslProtocolsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.ssl_protocol.deserialize_xml(child))
    return out
