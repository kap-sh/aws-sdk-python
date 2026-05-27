"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.default_retention


class ObjectLockRule(TypedDict):
    default_retention: NotRequired[
        "aws_sdk_s3.types.default_retention.DefaultRetention"
    ]
    """<p>The default Object Lock retention mode and period that you want to apply to new objects placed in the specified bucket. Bucket settings require both a mode and a period. The period can be either <code>Days</code> or <code>Years</code> but you must select one. You cannot specify <code>Days</code> and <code>Years</code> at the same time.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLockRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "default_retention" in value:
        import aws_sdk_s3.types.default_retention

        aws_sdk_s3.types.default_retention.serialize_xml(
            value["default_retention"], el, "DefaultRetention"
        )


def deserialize_xml(el: Element) -> ObjectLockRule:
    out: ObjectLockRule = {}  # type: ignore[typeddict-item]
    child_default_retention = el.find("DefaultRetention")
    if child_default_retention is not None:
        import aws_sdk_s3.types.default_retention

        out["default_retention"] = aws_sdk_s3.types.default_retention.deserialize_xml(
            child_default_retention
        )
    return out
