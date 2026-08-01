"""Generated from Smithy shape ``com.amazonaws.s3#NoncurrentVersionTransitionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.noncurrent_version_transition

NoncurrentVersionTransitionList: TypeAlias = list[
    "capo_s3.types.noncurrent_version_transition.NoncurrentVersionTransition"
]


# --- restXml ser/de ---
def serialize_xml(
    value: NoncurrentVersionTransitionList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.noncurrent_version_transition

        capo_s3.types.noncurrent_version_transition.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> NoncurrentVersionTransitionList:
    import capo_s3.types.noncurrent_version_transition

    out: NoncurrentVersionTransitionList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.noncurrent_version_transition.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: NoncurrentVersionTransitionList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.noncurrent_version_transition

        capo_s3.types.noncurrent_version_transition.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> NoncurrentVersionTransitionList:
    import capo_s3.types.noncurrent_version_transition

    out: NoncurrentVersionTransitionList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.noncurrent_version_transition.deserialize_xml(child))
    return out
