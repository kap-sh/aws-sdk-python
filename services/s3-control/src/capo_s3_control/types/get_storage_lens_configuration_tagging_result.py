"""Generated from Smithy shape ``com.amazonaws.s3control#GetStorageLensConfigurationTaggingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_tags


class GetStorageLensConfigurationTaggingResult(TypedDict, closed=True):
    tags: NotRequired["capo_s3_control.types.storage_lens_tags.StorageLensTags"]
    """<p>The tags of S3 Storage Lens configuration requested.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStorageLensConfigurationTaggingResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "tags" in value:
        import capo_s3_control.types.storage_lens_tags

        capo_s3_control.types.storage_lens_tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> GetStorageLensConfigurationTaggingResult:
    out: GetStorageLensConfigurationTaggingResult = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.storage_lens_tags

        out["tags"] = capo_s3_control.types.storage_lens_tags.deserialize_xml(
            child_tags
        )
    return out
