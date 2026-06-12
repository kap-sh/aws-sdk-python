"""Generated from Smithy shape ``com.amazonaws.s3control#SubmitMultiRegionAccessPointRoutesResult``."""

from typing import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class SubmitMultiRegionAccessPointRoutesResult(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: SubmitMultiRegionAccessPointRoutesResult, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> SubmitMultiRegionAccessPointRoutesResult:
    out: SubmitMultiRegionAccessPointRoutesResult = {}  # type: ignore[typeddict-item]
    return out
