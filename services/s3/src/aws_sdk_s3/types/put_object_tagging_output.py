"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectTaggingOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_version_id


class PutObjectTaggingOutput(TypedDict):
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>The versionId of the object the tag-set was added to.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutObjectTaggingOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PutObjectTaggingOutput:
    out: PutObjectTaggingOutput = {}  # type: ignore[typeddict-item]
    return out
