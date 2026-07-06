"""Generated from Smithy shape ``com.amazonaws.s3control#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.s3_resource_arn
    import aws_sdk_s3_control.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that owns the resource that you're trying to remove the tags from. </p>"""
    resource_arn: "aws_sdk_s3_control.types.s3_resource_arn.S3ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the S3 resource that you're removing tags from. The tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance, registered location, or grant.</p>"""
    tag_keys: "aws_sdk_s3_control.types.tag_key_list.TagKeyList"
    """<p> The array of tag key-value pairs that you're trying to remove from of the S3 resource. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: UntagResourceRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
