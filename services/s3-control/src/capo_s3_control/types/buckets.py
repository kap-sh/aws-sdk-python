"""Generated from Smithy shape ``com.amazonaws.s3control#Buckets``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_bucket_arn_string

Buckets: TypeAlias = list[
    "capo_s3_control.types.s3_bucket_arn_string.S3BucketArnString"
]


# --- restXml ser/de ---
def serialize_xml(value: Buckets, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Arn").text = str(item)


def deserialize_xml(el: Element) -> Buckets:
    out: Buckets = []
    for child in el.findall("Arn"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: Buckets, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> Buckets:
    out: Buckets = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
