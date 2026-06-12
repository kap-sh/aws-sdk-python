"""Generated from Smithy shape ``com.amazonaws.s3control#S3Retention``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_object_lock_retention_mode
    import aws_sdk_s3_control.types.time_stamp


class S3Retention(TypedDict):
    retain_until_date: NotRequired["aws_sdk_s3_control.types.time_stamp.TimeStamp"]
    """<p>The date when the applied Object Lock retention will expire on all objects set by the Batch Operations job.</p>"""
    mode: NotRequired[
        "aws_sdk_s3_control.types.s3_object_lock_retention_mode.S3ObjectLockRetentionMode"
    ]
    """<p>The Object Lock retention mode to be applied to all objects in the Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Retention, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "retain_until_date" in value:
        import aws_sdk_s3_control.types.time_stamp

        aws_sdk_s3_control.types.time_stamp.serialize_xml(
            value["retain_until_date"], el, "RetainUntilDate"
        )
    if "mode" in value:
        import aws_sdk_s3_control.types.s3_object_lock_retention_mode

        aws_sdk_s3_control.types.s3_object_lock_retention_mode.serialize_xml(
            value["mode"], el, "Mode"
        )


def deserialize_xml(el: Element) -> S3Retention:
    out: S3Retention = {}  # type: ignore[typeddict-item]
    child_retain_until_date = el.find("RetainUntilDate")
    if child_retain_until_date is not None:
        import aws_sdk_s3_control.types.time_stamp

        out["retain_until_date"] = aws_sdk_s3_control.types.time_stamp.deserialize_xml(
            child_retain_until_date
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_s3_control.types.s3_object_lock_retention_mode

        out["mode"] = (
            aws_sdk_s3_control.types.s3_object_lock_retention_mode.deserialize_xml(
                child_mode
            )
        )
    return out
