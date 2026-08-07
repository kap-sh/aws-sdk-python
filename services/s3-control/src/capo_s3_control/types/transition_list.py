"""Generated from Smithy shape ``com.amazonaws.s3control#TransitionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.transition

TransitionList: TypeAlias = list["capo_s3_control.types.transition.Transition"]


# --- restXml ser/de ---
def serialize_xml(value: TransitionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.transition

        capo_s3_control.types.transition.serialize_xml(item, el, "Transition")


def deserialize_xml(el: Element) -> TransitionList:
    import capo_s3_control.types.transition

    out: TransitionList = []
    for child in el.findall("Transition"):
        out.append(capo_s3_control.types.transition.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TransitionList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.transition

        capo_s3_control.types.transition.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TransitionList:
    import capo_s3_control.types.transition

    out: TransitionList = []
    for child in parent.findall(tag):
        out.append(capo_s3_control.types.transition.deserialize_xml(child))
    return out
