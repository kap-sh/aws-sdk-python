"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteStorageLensConfigurationTaggingResult``."""

from typing import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement


class DeleteStorageLensConfigurationTaggingResult(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteStorageLensConfigurationTaggingResult, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteStorageLensConfigurationTaggingResult:
    out: DeleteStorageLensConfigurationTaggingResult = {}  # type: ignore[typeddict-item]
    return out
