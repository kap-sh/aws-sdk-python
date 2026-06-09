"""Generated from Smithy shape ``com.amazonaws.s3#LifecycleExpiration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.date
    import aws_sdk_s3.types.days
    import aws_sdk_s3.types.expired_object_delete_marker


class LifecycleExpiration(TypedDict):
    date: NotRequired["aws_sdk_s3.types.date.Date"]
    """<p>Indicates at what date the object is to be moved or deleted. The date value must conform to the ISO 8601 format. The time is always midnight UTC.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""
    days: NotRequired["aws_sdk_s3.types.days.Days"]
    """<p>Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.</p>"""
    expired_object_delete_marker: NotRequired[
        "aws_sdk_s3.types.expired_object_delete_marker.ExpiredObjectDeleteMarker"
    ]
    """<p>Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: LifecycleExpiration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "date" in value:
        import aws_sdk_s3.types.date

        aws_sdk_s3.types.date.serialize_xml(value["date"], el, "Date")
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])
    if "expired_object_delete_marker" in value:
        SubElement(el, "ExpiredObjectDeleteMarker").text = (
            "true" if value["expired_object_delete_marker"] else "false"
        )


def deserialize_xml(el: Element) -> LifecycleExpiration:
    out: LifecycleExpiration = {}  # type: ignore[typeddict-item]
    child_date = el.find("Date")
    if child_date is not None:
        import aws_sdk_s3.types.date

        out["date"] = aws_sdk_s3.types.date.deserialize_xml(child_date)
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    child_expired_object_delete_marker = el.find("ExpiredObjectDeleteMarker")
    if child_expired_object_delete_marker is not None:
        out["expired_object_delete_marker"] = (
            child_expired_object_delete_marker.text or ""
        ).lower() == "true"
    return out
