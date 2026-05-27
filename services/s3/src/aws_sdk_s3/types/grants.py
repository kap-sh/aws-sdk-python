"""Generated from Smithy shape ``com.amazonaws.s3#Grants``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.grant

Grants: TypeAlias = list["aws_sdk_s3.types.grant.Grant"]


# --- restXml ser/de ---
def serialize_xml(value: Grants, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.grant

        aws_sdk_s3.types.grant.serialize_xml(item, el, "Grant")


def deserialize_xml(el: Element) -> Grants:
    import aws_sdk_s3.types.grant

    out: Grants = []
    for child in el.findall("Grant"):
        out.append(aws_sdk_s3.types.grant.deserialize_xml(child))
    return out


def serialize_xml_flat(value: Grants, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.grant

        aws_sdk_s3.types.grant.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> Grants:
    import aws_sdk_s3.types.grant

    out: Grants = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.grant.deserialize_xml(child))
    return out
