"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringAndOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.prefix
    import capo_s3.types.tag_set


class IntelligentTieringAndOperator(TypedDict, closed=True):
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>An object key name prefix that identifies the subset of objects to which the configuration applies.</p>"""
    tags: NotRequired["capo_s3.types.tag_set.TagSet"]
    """<p>All of these tags must exist in the object's tag set in order for the configuration to apply.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: IntelligentTieringAndOperator, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tags" in value:
        import capo_s3.types.tag_set

        capo_s3.types.tag_set.serialize_xml_flat(value["tags"], el, "Tag")


def deserialize_xml(el: Element) -> IntelligentTieringAndOperator:
    out: IntelligentTieringAndOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    if el.find("Tag") is not None:
        import capo_s3.types.tag_set

        out["tags"] = capo_s3.types.tag_set.deserialize_xml_flat(el, "Tag")
    return out
