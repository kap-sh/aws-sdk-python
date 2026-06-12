"""Generated from Smithy shape ``com.amazonaws.s3control#MatchAnyTag``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_tag

MatchAnyTag: TypeAlias = list["aws_sdk_s3_control.types.s3_tag.S3Tag"]


# --- restXml ser/de ---
def serialize_xml(value: MatchAnyTag, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.s3_tag

        aws_sdk_s3_control.types.s3_tag.serialize_xml(item, el, "Tag")


def deserialize_xml(el: Element) -> MatchAnyTag:
    import aws_sdk_s3_control.types.s3_tag

    out: MatchAnyTag = []
    for child in el.findall("Tag"):
        out.append(aws_sdk_s3_control.types.s3_tag.deserialize_xml(child))
    return out


def serialize_xml_flat(value: MatchAnyTag, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.s3_tag

        aws_sdk_s3_control.types.s3_tag.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> MatchAnyTag:
    import aws_sdk_s3_control.types.s3_tag

    out: MatchAnyTag = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3_control.types.s3_tag.deserialize_xml(child))
    return out
