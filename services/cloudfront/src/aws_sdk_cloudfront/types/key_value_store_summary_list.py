"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyValueStoreSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_value_store

KeyValueStoreSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.key_value_store.KeyValueStore"
]


# --- restXml ser/de ---
def serialize_xml(value: KeyValueStoreSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.key_value_store

        aws_sdk_cloudfront.types.key_value_store.serialize_xml(
            item, el, "KeyValueStore"
        )


def deserialize_xml(el: Element) -> KeyValueStoreSummaryList:
    import aws_sdk_cloudfront.types.key_value_store

    out: KeyValueStoreSummaryList = []
    for child in el.findall("KeyValueStore"):
        out.append(aws_sdk_cloudfront.types.key_value_store.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: KeyValueStoreSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.key_value_store

        aws_sdk_cloudfront.types.key_value_store.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> KeyValueStoreSummaryList:
    import aws_sdk_cloudfront.types.key_value_store

    out: KeyValueStoreSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.key_value_store.deserialize_xml(child))
    return out
