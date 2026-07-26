"""Generated from Smithy shape ``com.amazonaws.s3control#MatchObjectAge``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_age_value


class MatchObjectAge(TypedDict, closed=True):
    days_greater_than: "capo_s3_control.types.object_age_value.ObjectAgeValue"
    """<p> Specifies the maximum object age in days. Must be a positive whole number, greater than the minimum object age and less than or equal to 2,147,483,647. </p>"""
    days_less_than: "capo_s3_control.types.object_age_value.ObjectAgeValue"
    """<p> Specifies the minimum object age in days. The value must be a positive whole number, greater than 0 and less than or equal to 2,147,483,647. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: MatchObjectAge, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "DaysGreaterThan").text = str(value.get("days_greater_than", 0))
    SubElement(el, "DaysLessThan").text = str(value.get("days_less_than", 0))


def deserialize_xml(el: Element) -> MatchObjectAge:
    out: MatchObjectAge = {}  # type: ignore[typeddict-item]
    child_days_greater_than = el.find("DaysGreaterThan")
    if child_days_greater_than is not None:
        out["days_greater_than"] = int(child_days_greater_than.text or "")
    else:
        out["days_greater_than"] = 0
    child_days_less_than = el.find("DaysLessThan")
    if child_days_less_than is not None:
        out["days_less_than"] = int(child_days_less_than.text or "")
    else:
        out["days_less_than"] = 0
    return out
