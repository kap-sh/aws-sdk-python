"""Generated from Smithy shape ``com.amazonaws.s3control#S3TagSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_tag

S3TagSet: TypeAlias = list["capo_s3_control.types.s3_tag.S3Tag"]


# --- restXml ser/de ---
def serialize_xml(value: S3TagSet, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.s3_tag

        capo_s3_control.types.s3_tag.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> S3TagSet:
    import capo_s3_control.types.s3_tag

    out: S3TagSet = []
    for child in el.findall("member"):
        out.append(capo_s3_control.types.s3_tag.deserialize_xml(child))
    return out


def serialize_xml_flat(value: S3TagSet, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.s3_tag

        capo_s3_control.types.s3_tag.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> S3TagSet:
    import capo_s3_control.types.s3_tag

    out: S3TagSet = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.s3_tag.deserialize_xml(child))
    return out
