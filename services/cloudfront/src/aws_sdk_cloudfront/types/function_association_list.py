"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_association

FunctionAssociationList: TypeAlias = list[
    "aws_sdk_cloudfront.types.function_association.FunctionAssociation"
]


# --- restXml ser/de ---
def serialize_xml(value: FunctionAssociationList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.function_association

        aws_sdk_cloudfront.types.function_association.serialize_xml(
            item, el, "FunctionAssociation"
        )


def deserialize_xml(el: Element) -> FunctionAssociationList:
    import aws_sdk_cloudfront.types.function_association

    out: FunctionAssociationList = []
    for child in el.findall("FunctionAssociation"):
        out.append(aws_sdk_cloudfront.types.function_association.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: FunctionAssociationList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.function_association

        aws_sdk_cloudfront.types.function_association.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> FunctionAssociationList:
    import aws_sdk_cloudfront.types.function_association

    out: FunctionAssociationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.function_association.deserialize_xml(child))
    return out
