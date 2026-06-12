"""Generated from Smithy shape ``com.amazonaws.s3control#PutJobTaggingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.job_id
    import aws_sdk_s3_control.types.s3_tag_set


class PutJobTaggingRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>"""
    job_id: "aws_sdk_s3_control.types.job_id.JobId"
    """<p>The ID for the S3 Batch Operations job whose tags you want to replace.</p>"""
    tags: "aws_sdk_s3_control.types.s3_tag_set.S3TagSet"
    """<p>The set of tags to associate with the S3 Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutJobTaggingRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.s3_tag_set

    aws_sdk_s3_control.types.s3_tag_set.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> PutJobTaggingRequest:
    out: PutJobTaggingRequest = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_s3_control.types.s3_tag_set

        out["tags"] = aws_sdk_s3_control.types.s3_tag_set.deserialize_xml(child_tags)
    else:
        raise DeserializationError("PutJobTaggingRequest.tags required")
    return out
