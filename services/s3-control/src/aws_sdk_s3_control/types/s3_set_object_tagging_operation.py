"""Generated from Smithy shape ``com.amazonaws.s3control#S3SetObjectTaggingOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_tag_set


class S3SetObjectTaggingOperation(TypedDict, closed=True):
    tag_set: NotRequired["aws_sdk_s3_control.types.s3_tag_set.S3TagSet"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3SetObjectTaggingOperation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "tag_set" in value:
        import aws_sdk_s3_control.types.s3_tag_set

        aws_sdk_s3_control.types.s3_tag_set.serialize_xml(
            value["tag_set"], el, "TagSet"
        )


def deserialize_xml(el: Element) -> S3SetObjectTaggingOperation:
    out: S3SetObjectTaggingOperation = {}  # type: ignore[typeddict-item]
    child_tag_set = el.find("TagSet")
    if child_tag_set is not None:
        import aws_sdk_s3_control.types.s3_tag_set

        out["tag_set"] = aws_sdk_s3_control.types.s3_tag_set.deserialize_xml(
            child_tag_set
        )
    return out
