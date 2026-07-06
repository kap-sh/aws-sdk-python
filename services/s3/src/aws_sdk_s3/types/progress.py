"""Generated from Smithy shape ``com.amazonaws.s3#Progress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bytes_processed
    import aws_sdk_s3.types.bytes_returned
    import aws_sdk_s3.types.bytes_scanned


class Progress(TypedDict, closed=True):
    bytes_scanned: NotRequired["aws_sdk_s3.types.bytes_scanned.BytesScanned"]
    """<p>The current number of object bytes scanned.</p>"""
    bytes_processed: NotRequired["aws_sdk_s3.types.bytes_processed.BytesProcessed"]
    """<p>The current number of uncompressed object bytes processed.</p>"""
    bytes_returned: NotRequired["aws_sdk_s3.types.bytes_returned.BytesReturned"]
    """<p>The current number of bytes of records payload data returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Progress, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bytes_scanned" in value:
        SubElement(el, "BytesScanned").text = str(value["bytes_scanned"])
    if "bytes_processed" in value:
        SubElement(el, "BytesProcessed").text = str(value["bytes_processed"])
    if "bytes_returned" in value:
        SubElement(el, "BytesReturned").text = str(value["bytes_returned"])


def deserialize_xml(el: Element) -> Progress:
    out: Progress = {}  # type: ignore[typeddict-item]
    child_bytes_scanned = el.find("BytesScanned")
    if child_bytes_scanned is not None:
        out["bytes_scanned"] = int(child_bytes_scanned.text or "")
    child_bytes_processed = el.find("BytesProcessed")
    if child_bytes_processed is not None:
        out["bytes_processed"] = int(child_bytes_processed.text or "")
    child_bytes_returned = el.find("BytesReturned")
    if child_bytes_returned is not None:
        out["bytes_returned"] = int(child_bytes_returned.text or "")
    return out
