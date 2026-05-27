"""Generated from Smithy shape ``com.amazonaws.s3#InventoryOptionalFields``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.inventory_optional_field

InventoryOptionalFields: TypeAlias = list[
    "aws_sdk_s3.types.inventory_optional_field.InventoryOptionalField"
]


# --- restXml ser/de ---
def serialize_xml(value: InventoryOptionalFields, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.inventory_optional_field

        aws_sdk_s3.types.inventory_optional_field.serialize_xml(item, el, "Field")


def deserialize_xml(el: Element) -> InventoryOptionalFields:
    import aws_sdk_s3.types.inventory_optional_field

    out: InventoryOptionalFields = []
    for child in el.findall("Field"):
        out.append(aws_sdk_s3.types.inventory_optional_field.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: InventoryOptionalFields, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.inventory_optional_field

        aws_sdk_s3.types.inventory_optional_field.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> InventoryOptionalFields:
    import aws_sdk_s3.types.inventory_optional_field

    out: InventoryOptionalFields = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.inventory_optional_field.deserialize_xml(child))
    return out
