"""Generated from Smithy shape ``com.amazonaws.s3#DeleteObjectTaggingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_version_id


class DeleteObjectTaggingOutput(TypedDict, closed=True):
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>The versionId of the object the tag-set was removed from.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteObjectTaggingOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteObjectTaggingOutput:
    out: DeleteObjectTaggingOutput = {}  # type: ignore[typeddict-item]
    return out
