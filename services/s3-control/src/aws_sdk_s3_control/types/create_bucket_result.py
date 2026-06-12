"""Generated from Smithy shape ``com.amazonaws.s3control#CreateBucketResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.location
    import aws_sdk_s3_control.types.s3_regional_bucket_arn


class CreateBucketResult(TypedDict):
    location: NotRequired["aws_sdk_s3_control.types.location.Location"]
    """<p>The location of the bucket.</p>"""
    bucket_arn: NotRequired[
        "aws_sdk_s3_control.types.s3_regional_bucket_arn.S3RegionalBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateBucketResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bucket_arn" in value:
        SubElement(el, "BucketArn").text = str(value["bucket_arn"])


def deserialize_xml(el: Element) -> CreateBucketResult:
    out: CreateBucketResult = {}  # type: ignore[typeddict-item]
    child_bucket_arn = el.find("BucketArn")
    if child_bucket_arn is not None:
        out["bucket_arn"] = str(child_bucket_arn.text or "")
    return out
