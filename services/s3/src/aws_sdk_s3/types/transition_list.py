"""Generated from Smithy shape ``com.amazonaws.s3#TransitionList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.transition

TransitionList: TypeAlias = list["aws_sdk_s3.types.transition.Transition"]


# --- restXml ser/de ---
def serialize_xml(value: TransitionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.transition

        aws_sdk_s3.types.transition.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> TransitionList:
    import aws_sdk_s3.types.transition

    out: TransitionList = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3.types.transition.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TransitionList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.transition

        aws_sdk_s3.types.transition.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TransitionList:
    import aws_sdk_s3.types.transition

    out: TransitionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.transition.deserialize_xml(child))
    return out
