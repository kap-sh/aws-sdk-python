"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationTimeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.minutes


class ReplicationTimeValue(TypedDict, closed=True):
    minutes: NotRequired["aws_sdk_s3.types.minutes.Minutes"]
    """<p> Contains an integer specifying time in minutes. </p> <p> Valid value: 15</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicationTimeValue, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "minutes" in value:
        SubElement(el, "Minutes").text = str(value["minutes"])


def deserialize_xml(el: Element) -> ReplicationTimeValue:
    out: ReplicationTimeValue = {}  # type: ignore[typeddict-item]
    child_minutes = el.find("Minutes")
    if child_minutes is not None:
        out["minutes"] = int(child_minutes.text or "")
    return out
