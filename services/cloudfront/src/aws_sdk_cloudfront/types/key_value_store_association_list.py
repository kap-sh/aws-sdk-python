"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyValueStoreAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_value_store_association

KeyValueStoreAssociationList: TypeAlias = list[
    "aws_sdk_cloudfront.types.key_value_store_association.KeyValueStoreAssociation"
]


# --- restXml ser/de ---
def serialize_xml(
    value: KeyValueStoreAssociationList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.key_value_store_association

        aws_sdk_cloudfront.types.key_value_store_association.serialize_xml(
            item, el, "KeyValueStoreAssociation"
        )


def deserialize_xml(el: Element) -> KeyValueStoreAssociationList:
    import aws_sdk_cloudfront.types.key_value_store_association

    out: KeyValueStoreAssociationList = []
    for child in el.findall("KeyValueStoreAssociation"):
        out.append(
            aws_sdk_cloudfront.types.key_value_store_association.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: KeyValueStoreAssociationList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.key_value_store_association

        aws_sdk_cloudfront.types.key_value_store_association.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> KeyValueStoreAssociationList:
    import aws_sdk_cloudfront.types.key_value_store_association

    out: KeyValueStoreAssociationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.key_value_store_association.deserialize_xml(child)
        )
    return out
