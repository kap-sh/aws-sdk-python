"""Generated from Smithy shape ``com.amazonaws.s3#ScanRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.end
    import aws_sdk_s3.types.start


class ScanRange(TypedDict):
    start: NotRequired["aws_sdk_s3.types.start.Start"]
    """<p>Specifies the start of the byte range. This parameter is optional. Valid values: non-negative integers. The default value is 0. If only <code>start</code> is supplied, it means scan from that point to the end of the file. For example, <code><scanrange><start>50</start></scanrange></code> means scan from byte 50 until the end of the file.</p>"""
    end: NotRequired["aws_sdk_s3.types.end.End"]
    """<p>Specifies the end of the byte range. This parameter is optional. Valid values: non-negative integers. The default value is one less than the size of the object being queried. If only the End parameter is supplied, it is interpreted to mean scan the last N bytes of the file. For example, <code><scanrange><end>50</end></scanrange></code> means scan the last 50 bytes.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ScanRange, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "start" in value:
        SubElement(el, "Start").text = str(value["start"])
    if "end" in value:
        SubElement(el, "End").text = str(value["end"])


def deserialize_xml(el: Element) -> ScanRange:
    out: ScanRange = {}  # type: ignore[typeddict-item]
    child_start = el.find("Start")
    if child_start is not None:
        out["start"] = int(child_start.text or "")
    child_end = el.find("End")
    if child_end is not None:
        out["end"] = int(child_end.text or "")
    return out
