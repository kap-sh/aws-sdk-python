"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteStorageLensConfigurationTaggingResult``."""

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement


class DeleteStorageLensConfigurationTaggingResult(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteStorageLensConfigurationTaggingResult, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteStorageLensConfigurationTaggingResult:
    out: DeleteStorageLensConfigurationTaggingResult = {}  # type: ignore[typeddict-item]
    return out
