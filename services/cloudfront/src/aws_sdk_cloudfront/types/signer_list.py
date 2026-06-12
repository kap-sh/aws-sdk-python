"""Generated from Smithy shape ``com.amazonaws.cloudfront#SignerList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.signer

SignerList: TypeAlias = list["aws_sdk_cloudfront.types.signer.Signer"]


# --- restXml ser/de ---
def serialize_xml(value: SignerList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.signer

        aws_sdk_cloudfront.types.signer.serialize_xml(item, el, "Signer")


def deserialize_xml(el: Element) -> SignerList:
    import aws_sdk_cloudfront.types.signer

    out: SignerList = []
    for child in el.findall("Signer"):
        out.append(aws_sdk_cloudfront.types.signer.deserialize_xml(child))
    return out


def serialize_xml_flat(value: SignerList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.signer

        aws_sdk_cloudfront.types.signer.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> SignerList:
    import aws_sdk_cloudfront.types.signer

    out: SignerList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.signer.deserialize_xml(child))
    return out
