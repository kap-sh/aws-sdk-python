"""Generated from Smithy shape ``com.amazonaws.s3control#PutJobTaggingResult``."""

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class PutJobTaggingResult(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: PutJobTaggingResult, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PutJobTaggingResult:
    out: PutJobTaggingResult = {}  # type: ignore[typeddict-item]
    return out
