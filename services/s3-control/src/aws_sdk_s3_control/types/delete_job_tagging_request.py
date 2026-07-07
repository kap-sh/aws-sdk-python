"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteJobTaggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.job_id


class DeleteJobTaggingRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>"""
    job_id: "aws_sdk_s3_control.types.job_id.JobId"
    """<p>The ID for the S3 Batch Operations job whose tags you want to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteJobTaggingRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteJobTaggingRequest:
    out: DeleteJobTaggingRequest = {}  # type: ignore[typeddict-item]
    return out
