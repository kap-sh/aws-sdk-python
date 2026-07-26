"""Generated from Smithy shape ``com.amazonaws.s3#LifecycleRuleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.lifecycle_rule_and_operator
    import capo_s3.types.object_size_greater_than_bytes
    import capo_s3.types.object_size_less_than_bytes
    import capo_s3.types.prefix
    import capo_s3.types.tag

LifecycleRuleFilter = TypedDict(
    "LifecycleRuleFilter",
    {
        "prefix": NotRequired["capo_s3.types.prefix.Prefix"],
        "tag": NotRequired["capo_s3.types.tag.Tag"],
        "object_size_greater_than": NotRequired[
            "capo_s3.types.object_size_greater_than_bytes.ObjectSizeGreaterThanBytes"
        ],
        "object_size_less_than": NotRequired[
            "capo_s3.types.object_size_less_than_bytes.ObjectSizeLessThanBytes"
        ],
        "and": NotRequired[
            "capo_s3.types.lifecycle_rule_and_operator.LifecycleRuleAndOperator"
        ],
    },
    closed=True,
)


# --- restXml ser/de ---
def serialize_xml(value: LifecycleRuleFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tag" in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(value["tag"], el, "Tag")
    if "object_size_greater_than" in value:
        SubElement(el, "ObjectSizeGreaterThan").text = str(
            value["object_size_greater_than"]
        )
    if "object_size_less_than" in value:
        SubElement(el, "ObjectSizeLessThan").text = str(value["object_size_less_than"])
    if "and" in value:
        import capo_s3.types.lifecycle_rule_and_operator

        capo_s3.types.lifecycle_rule_and_operator.serialize_xml(value["and"], el, "And")


def deserialize_xml(el: Element) -> LifecycleRuleFilter:
    out: LifecycleRuleFilter = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tag = el.find("Tag")
    if child_tag is not None:
        import capo_s3.types.tag

        out["tag"] = capo_s3.types.tag.deserialize_xml(child_tag)
    child_object_size_greater_than = el.find("ObjectSizeGreaterThan")
    if child_object_size_greater_than is not None:
        out["object_size_greater_than"] = int(child_object_size_greater_than.text or "")
    child_object_size_less_than = el.find("ObjectSizeLessThan")
    if child_object_size_less_than is not None:
        out["object_size_less_than"] = int(child_object_size_less_than.text or "")
    child_and = el.find("And")
    if child_and is not None:
        import capo_s3.types.lifecycle_rule_and_operator

        out["and"] = capo_s3.types.lifecycle_rule_and_operator.deserialize_xml(
            child_and
        )
    return out
