"""Generated from Smithy shape ``com.amazonaws.s3#DefaultRetention``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.days
    import capo_s3.types.object_lock_retention_mode
    import capo_s3.types.years


class DefaultRetention(TypedDict, closed=True):
    mode: NotRequired[
        "capo_s3.types.object_lock_retention_mode.ObjectLockRetentionMode"
    ]
    """<p>The default Object Lock retention mode you want to apply to new objects placed in the specified bucket. Must be used with either <code>Days</code> or <code>Years</code>.</p>"""
    days: NotRequired["capo_s3.types.days.Days"]
    """<p>The number of days that you want to specify for the default retention period. Must be used with <code>Mode</code>.</p>"""
    years: NotRequired["capo_s3.types.years.Years"]
    """<p>The number of years that you want to specify for the default retention period. Must be used with <code>Mode</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DefaultRetention, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "mode" in value:
        import capo_s3.types.object_lock_retention_mode

        capo_s3.types.object_lock_retention_mode.serialize_xml(
            value["mode"], el, "Mode"
        )
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])
    if "years" in value:
        SubElement(el, "Years").text = str(value["years"])


def deserialize_xml(el: Element) -> DefaultRetention:
    out: DefaultRetention = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_s3.types.object_lock_retention_mode

        out["mode"] = capo_s3.types.object_lock_retention_mode.deserialize_xml(
            child_mode
        )
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    child_years = el.find("Years")
    if child_years is not None:
        out["years"] = int(child_years.text or "")
    return out
