"""Generated from Smithy shape ``com.amazonaws.s3control#PutStorageLensConfigurationTaggingResult``."""

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement


class PutStorageLensConfigurationTaggingResult(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: PutStorageLensConfigurationTaggingResult, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PutStorageLensConfigurationTaggingResult:
    out: PutStorageLensConfigurationTaggingResult = {}  # type: ignore[typeddict-item]
    return out
