"""Generated from Smithy shape ``com.amazonaws.s3#LifecycleRuleAndOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_size_greater_than_bytes
    import capo_s3.types.object_size_less_than_bytes
    import capo_s3.types.prefix
    import capo_s3.types.tag_set


class LifecycleRuleAndOperator(TypedDict, closed=True):
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Prefix identifying one or more objects to which the rule applies.</p>"""
    tags: NotRequired["capo_s3.types.tag_set.TagSet"]
    """<p>All of these tags must exist in the object's tag set in order for the rule to apply.</p>"""
    object_size_greater_than: NotRequired[
        "capo_s3.types.object_size_greater_than_bytes.ObjectSizeGreaterThanBytes"
    ]
    """<p>Minimum object size to which the rule applies.</p>"""
    object_size_less_than: NotRequired[
        "capo_s3.types.object_size_less_than_bytes.ObjectSizeLessThanBytes"
    ]
    """<p>Maximum object size to which the rule applies.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LifecycleRuleAndOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tags" in value:
        import capo_s3.types.tag_set

        capo_s3.types.tag_set.serialize_xml_flat(value["tags"], el, "Tag")
    if "object_size_greater_than" in value:
        SubElement(el, "ObjectSizeGreaterThan").text = str(
            value["object_size_greater_than"]
        )
    if "object_size_less_than" in value:
        SubElement(el, "ObjectSizeLessThan").text = str(value["object_size_less_than"])


def deserialize_xml(el: Element) -> LifecycleRuleAndOperator:
    out: LifecycleRuleAndOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    if el.find("Tag") is not None:
        import capo_s3.types.tag_set

        out["tags"] = capo_s3.types.tag_set.deserialize_xml_flat(el, "Tag")
    child_object_size_greater_than = el.find("ObjectSizeGreaterThan")
    if child_object_size_greater_than is not None:
        out["object_size_greater_than"] = int(child_object_size_greater_than.text or "")
    child_object_size_less_than = el.find("ObjectSizeLessThan")
    if child_object_size_less_than is not None:
        out["object_size_less_than"] = int(child_object_size_less_than.text or "")
    return out
