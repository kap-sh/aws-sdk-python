"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketTaggingResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_tag_set


class GetBucketTaggingResult(TypedDict):
    tag_set: "aws_sdk_s3_control.types.s3_tag_set.S3TagSet"
    """<p>The tags set of the Outposts bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketTaggingResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.s3_tag_set

    aws_sdk_s3_control.types.s3_tag_set.serialize_xml(value["tag_set"], el, "TagSet")


def deserialize_xml(el: Element) -> GetBucketTaggingResult:
    out: GetBucketTaggingResult = {}  # type: ignore[typeddict-item]
    child_tag_set = el.find("TagSet")
    if child_tag_set is not None:
        import aws_sdk_s3_control.types.s3_tag_set

        out["tag_set"] = aws_sdk_s3_control.types.s3_tag_set.deserialize_xml(
            child_tag_set
        )
    else:
        raise DeserializationError("GetBucketTaggingResult.tag_set required")
    return out
