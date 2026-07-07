"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteJobTaggingResult``."""

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class DeleteJobTaggingResult(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: DeleteJobTaggingResult, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteJobTaggingResult:
    out: DeleteJobTaggingResult = {}  # type: ignore[typeddict-item]
    return out
