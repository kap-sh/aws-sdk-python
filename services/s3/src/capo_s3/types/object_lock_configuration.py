"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_lock_enabled
    import capo_s3.types.object_lock_rule


class ObjectLockConfiguration(TypedDict, closed=True):
    object_lock_enabled: NotRequired[
        "capo_s3.types.object_lock_enabled.ObjectLockEnabled"
    ]
    """<p>Indicates whether this bucket has an Object Lock configuration enabled. Enable <code>ObjectLockEnabled</code> when you apply <code>ObjectLockConfiguration</code> to a bucket. </p>"""
    rule: NotRequired["capo_s3.types.object_lock_rule.ObjectLockRule"]
    """<p>Specifies the Object Lock rule for the specified object. Enable the this rule when you apply <code>ObjectLockConfiguration</code> to a bucket. Bucket settings require both a mode and a period. The period can be either <code>Days</code> or <code>Years</code> but you must select one. You cannot specify <code>Days</code> and <code>Years</code> at the same time.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLockConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "object_lock_enabled" in value:
        import capo_s3.types.object_lock_enabled

        capo_s3.types.object_lock_enabled.serialize_xml(
            value["object_lock_enabled"], el, "ObjectLockEnabled"
        )
    if "rule" in value:
        import capo_s3.types.object_lock_rule

        capo_s3.types.object_lock_rule.serialize_xml(value["rule"], el, "Rule")


def deserialize_xml(el: Element) -> ObjectLockConfiguration:
    out: ObjectLockConfiguration = {}  # type: ignore[typeddict-item]
    child_object_lock_enabled = el.find("ObjectLockEnabled")
    if child_object_lock_enabled is not None:
        import capo_s3.types.object_lock_enabled

        out["object_lock_enabled"] = capo_s3.types.object_lock_enabled.deserialize_xml(
            child_object_lock_enabled
        )
    child_rule = el.find("Rule")
    if child_rule is not None:
        import capo_s3.types.object_lock_rule

        out["rule"] = capo_s3.types.object_lock_rule.deserialize_xml(child_rule)
    return out
