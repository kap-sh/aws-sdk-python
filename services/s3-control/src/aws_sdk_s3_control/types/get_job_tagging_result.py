"""Generated from Smithy shape ``com.amazonaws.s3control#GetJobTaggingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_tag_set


class GetJobTaggingResult(TypedDict):
    tags: NotRequired["aws_sdk_s3_control.types.s3_tag_set.S3TagSet"]
    """<p>The set of tags associated with the S3 Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetJobTaggingResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "tags" in value:
        import aws_sdk_s3_control.types.s3_tag_set

        aws_sdk_s3_control.types.s3_tag_set.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> GetJobTaggingResult:
    out: GetJobTaggingResult = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_s3_control.types.s3_tag_set

        out["tags"] = aws_sdk_s3_control.types.s3_tag_set.deserialize_xml(child_tags)
    return out
