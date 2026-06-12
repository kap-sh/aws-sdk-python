"""Generated from Smithy shape ``com.amazonaws.cloudfront#MethodsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.method

MethodsList: TypeAlias = list["aws_sdk_cloudfront.types.method.Method"]


# --- restXml ser/de ---
def serialize_xml(value: MethodsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.method

        aws_sdk_cloudfront.types.method.serialize_xml(item, el, "Method")


def deserialize_xml(el: Element) -> MethodsList:
    import aws_sdk_cloudfront.types.method

    out: MethodsList = []
    for child in el.findall("Method"):
        out.append(aws_sdk_cloudfront.types.method.deserialize_xml(child))
    return out


def serialize_xml_flat(value: MethodsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.method

        aws_sdk_cloudfront.types.method.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> MethodsList:
    import aws_sdk_cloudfront.types.method

    out: MethodsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.method.deserialize_xml(child))
    return out
