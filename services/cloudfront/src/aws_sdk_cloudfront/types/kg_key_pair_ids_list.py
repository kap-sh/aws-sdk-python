"""Generated from Smithy shape ``com.amazonaws.cloudfront#KGKeyPairIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.kg_key_pair_ids

KGKeyPairIdsList: TypeAlias = list[
    "aws_sdk_cloudfront.types.kg_key_pair_ids.KGKeyPairIds"
]


# --- restXml ser/de ---
def serialize_xml(value: KGKeyPairIdsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.kg_key_pair_ids

        aws_sdk_cloudfront.types.kg_key_pair_ids.serialize_xml(item, el, "KeyGroup")


def deserialize_xml(el: Element) -> KGKeyPairIdsList:
    import aws_sdk_cloudfront.types.kg_key_pair_ids

    out: KGKeyPairIdsList = []
    for child in el.findall("KeyGroup"):
        out.append(aws_sdk_cloudfront.types.kg_key_pair_ids.deserialize_xml(child))
    return out


def serialize_xml_flat(value: KGKeyPairIdsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.kg_key_pair_ids

        aws_sdk_cloudfront.types.kg_key_pair_ids.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> KGKeyPairIdsList:
    import aws_sdk_cloudfront.types.kg_key_pair_ids

    out: KGKeyPairIdsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.kg_key_pair_ids.deserialize_xml(child))
    return out
