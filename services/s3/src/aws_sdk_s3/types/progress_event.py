"""Generated from Smithy shape ``com.amazonaws.s3#ProgressEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.progress


class ProgressEvent(TypedDict):
    details: NotRequired["aws_sdk_s3.types.progress.Progress"]
    """<p>The Progress event details.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ProgressEvent, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "details" in value:
        import aws_sdk_s3.types.progress

        aws_sdk_s3.types.progress.serialize_xml(value["details"], el, "Details")


def deserialize_xml(el: Element) -> ProgressEvent:
    out: ProgressEvent = {}  # type: ignore[typeddict-item]
    child_details = el.find("Details")
    if child_details is not None:
        import aws_sdk_s3.types.progress

        out["details"] = aws_sdk_s3.types.progress.deserialize_xml(child_details)
    return out
