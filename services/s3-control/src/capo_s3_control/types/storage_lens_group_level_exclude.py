"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroupLevelExclude``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_group_arn

StorageLensGroupLevelExclude: TypeAlias = list[
    "capo_s3_control.types.storage_lens_group_arn.StorageLensGroupArn"
]


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensGroupLevelExclude, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Arn").text = str(item)


def deserialize_xml(el: Element) -> StorageLensGroupLevelExclude:
    out: StorageLensGroupLevelExclude = []
    for child in el.findall("Arn"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(
    value: StorageLensGroupLevelExclude, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> StorageLensGroupLevelExclude:
    out: StorageLensGroupLevelExclude = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
