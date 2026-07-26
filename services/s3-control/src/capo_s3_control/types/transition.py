"""Generated from Smithy shape ``com.amazonaws.s3control#Transition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.date
    import capo_s3_control.types.days
    import capo_s3_control.types.transition_storage_class


class Transition(TypedDict, closed=True):
    date: NotRequired["capo_s3_control.types.date.Date"]
    """<p>Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.</p>"""
    days: "capo_s3_control.types.days.Days"
    """<p>Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.</p>"""
    storage_class: NotRequired[
        "capo_s3_control.types.transition_storage_class.TransitionStorageClass"
    ]
    """<p>The storage class to which you want the object to transition.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Transition, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "date" in value:
        import capo_s3_control.types.date

        capo_s3_control.types.date.serialize_xml(value["date"], el, "Date")
    SubElement(el, "Days").text = str(value.get("days", 0))
    if "storage_class" in value:
        import capo_s3_control.types.transition_storage_class

        capo_s3_control.types.transition_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> Transition:
    out: Transition = {}  # type: ignore[typeddict-item]
    child_date = el.find("Date")
    if child_date is not None:
        import capo_s3_control.types.date

        out["date"] = capo_s3_control.types.date.deserialize_xml(child_date)
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    else:
        out["days"] = 0
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3_control.types.transition_storage_class

        out["storage_class"] = (
            capo_s3_control.types.transition_storage_class.deserialize_xml(
                child_storage_class
            )
        )
    return out
