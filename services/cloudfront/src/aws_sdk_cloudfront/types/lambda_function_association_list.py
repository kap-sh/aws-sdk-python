"""Generated from Smithy shape ``com.amazonaws.cloudfront#LambdaFunctionAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.lambda_function_association

LambdaFunctionAssociationList: TypeAlias = list[
    "aws_sdk_cloudfront.types.lambda_function_association.LambdaFunctionAssociation"
]


# --- restXml ser/de ---
def serialize_xml(
    value: LambdaFunctionAssociationList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.lambda_function_association

        aws_sdk_cloudfront.types.lambda_function_association.serialize_xml(
            item, el, "LambdaFunctionAssociation"
        )


def deserialize_xml(el: Element) -> LambdaFunctionAssociationList:
    import aws_sdk_cloudfront.types.lambda_function_association

    out: LambdaFunctionAssociationList = []
    for child in el.findall("LambdaFunctionAssociation"):
        out.append(
            aws_sdk_cloudfront.types.lambda_function_association.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: LambdaFunctionAssociationList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.lambda_function_association

        aws_sdk_cloudfront.types.lambda_function_association.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> LambdaFunctionAssociationList:
    import aws_sdk_cloudfront.types.lambda_function_association

    out: LambdaFunctionAssociationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.lambda_function_association.deserialize_xml(child)
        )
    return out
