"""Generated from Smithy shape ``com.amazonaws.cloudfront#EncryptionEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.encryption_entity

EncryptionEntityList: TypeAlias = list[
    "capo_cloudfront.types.encryption_entity.EncryptionEntity"
]


# --- restXml ser/de ---
def serialize_xml(value: EncryptionEntityList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.encryption_entity

        capo_cloudfront.types.encryption_entity.serialize_xml(
            item, el, "EncryptionEntity"
        )


def deserialize_xml(el: Element) -> EncryptionEntityList:
    import capo_cloudfront.types.encryption_entity

    out: EncryptionEntityList = []
    for child in el.findall("EncryptionEntity"):
        out.append(capo_cloudfront.types.encryption_entity.deserialize_xml(child))
    return out


def serialize_xml_flat(value: EncryptionEntityList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.encryption_entity

        capo_cloudfront.types.encryption_entity.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> EncryptionEntityList:
    import capo_cloudfront.types.encryption_entity

    out: EncryptionEntityList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.encryption_entity.deserialize_xml(child))
    return out
