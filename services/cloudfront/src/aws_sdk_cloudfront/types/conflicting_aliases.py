"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConflictingAliases``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.conflicting_alias

ConflictingAliases: TypeAlias = list[
    "aws_sdk_cloudfront.types.conflicting_alias.ConflictingAlias"
]


# --- restXml ser/de ---
def serialize_xml(value: ConflictingAliases, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.conflicting_alias

        aws_sdk_cloudfront.types.conflicting_alias.serialize_xml(
            item, el, "ConflictingAlias"
        )


def deserialize_xml(el: Element) -> ConflictingAliases:
    import aws_sdk_cloudfront.types.conflicting_alias

    out: ConflictingAliases = []
    for child in el.findall("ConflictingAlias"):
        out.append(aws_sdk_cloudfront.types.conflicting_alias.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ConflictingAliases, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.conflicting_alias

        aws_sdk_cloudfront.types.conflicting_alias.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ConflictingAliases:
    import aws_sdk_cloudfront.types.conflicting_alias

    out: ConflictingAliases = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudfront.types.conflicting_alias.deserialize_xml(child))
    return out
