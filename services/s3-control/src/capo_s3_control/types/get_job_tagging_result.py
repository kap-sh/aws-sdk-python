"""Generated from Smithy shape ``com.amazonaws.s3control#GetJobTaggingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_tag_set


class GetJobTaggingResult(TypedDict, closed=True):
    tags: NotRequired["capo_s3_control.types.s3_tag_set.S3TagSet"]
    """<p>The set of tags associated with the S3 Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetJobTaggingResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "tags" in value:
        import capo_s3_control.types.s3_tag_set

        capo_s3_control.types.s3_tag_set.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> GetJobTaggingResult:
    out: GetJobTaggingResult = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.s3_tag_set

        out["tags"] = capo_s3_control.types.s3_tag_set.deserialize_xml(child_tags)
    return out
