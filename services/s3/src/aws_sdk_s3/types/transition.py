"""Generated from Smithy shape ``com.amazonaws.s3#Transition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.date
    import aws_sdk_s3.types.days
    import aws_sdk_s3.types.transition_storage_class


class Transition(TypedDict):
    date: NotRequired["aws_sdk_s3.types.date.Date"]
    """<p>Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.</p>"""
    days: NotRequired["aws_sdk_s3.types.days.Days"]
    """<p>Indicates the number of days after creation when objects are transitioned to the specified storage class. If the specified storage class is <code>INTELLIGENT_TIERING</code>, <code>GLACIER_IR</code>, <code>GLACIER</code>, or <code>DEEP_ARCHIVE</code>, valid values are <code>0</code> or positive integers. If the specified storage class is <code>STANDARD_IA</code> or <code>ONEZONE_IA</code>, valid values are positive integers greater than <code>30</code>. Be aware that some storage classes have a minimum storage duration and that you're charged for transitioning objects before their minimum storage duration. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html#lifecycle-configuration-constraints\"> Constraints and considerations for transitions</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    storage_class: NotRequired[
        "aws_sdk_s3.types.transition_storage_class.TransitionStorageClass"
    ]
    """<p>The storage class to which you want the object to transition.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Transition, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "date" in value:
        import aws_sdk_s3.types.date

        aws_sdk_s3.types.date.serialize_xml(value["date"], el, "Date")
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])
    if "storage_class" in value:
        import aws_sdk_s3.types.transition_storage_class

        aws_sdk_s3.types.transition_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> Transition:
    out: Transition = {}  # type: ignore[typeddict-item]
    child_date = el.find("Date")
    if child_date is not None:
        import aws_sdk_s3.types.date

        out["date"] = aws_sdk_s3.types.date.deserialize_xml(child_date)
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import aws_sdk_s3.types.transition_storage_class

        out["storage_class"] = (
            aws_sdk_s3.types.transition_storage_class.deserialize_xml(
                child_storage_class
            )
        )
    return out
