"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockRetention``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.date
    import aws_sdk_s3.types.object_lock_retention_mode


class ObjectLockRetention(TypedDict, closed=True):
    mode: NotRequired[
        "aws_sdk_s3.types.object_lock_retention_mode.ObjectLockRetentionMode"
    ]
    """<p>Indicates the Retention mode for the specified object.</p>"""
    retain_until_date: NotRequired["aws_sdk_s3.types.date.Date"]
    """<p>The date on which this Object Lock Retention will expire.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLockRetention, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "mode" in value:
        import aws_sdk_s3.types.object_lock_retention_mode

        aws_sdk_s3.types.object_lock_retention_mode.serialize_xml(
            value["mode"], el, "Mode"
        )
    if "retain_until_date" in value:
        import aws_sdk_s3.types.date

        aws_sdk_s3.types.date.serialize_xml(
            value["retain_until_date"], el, "RetainUntilDate"
        )


def deserialize_xml(el: Element) -> ObjectLockRetention:
    out: ObjectLockRetention = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_s3.types.object_lock_retention_mode

        out["mode"] = aws_sdk_s3.types.object_lock_retention_mode.deserialize_xml(
            child_mode
        )
    child_retain_until_date = el.find("RetainUntilDate")
    if child_retain_until_date is not None:
        import aws_sdk_s3.types.date

        out["retain_until_date"] = aws_sdk_s3.types.date.deserialize_xml(
            child_retain_until_date
        )
    return out
