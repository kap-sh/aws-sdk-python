"""Generated from Smithy shape ``com.amazonaws.s3#DeleteBucketMetadataConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name


class DeleteBucketMetadataConfigurationRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that you want to remove the metadata configuration from. </p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p> The expected bucket owner of the general purpose bucket that you want to remove the metadata table configuration from. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteBucketMetadataConfigurationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteBucketMetadataConfigurationRequest:
    out: DeleteBucketMetadataConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
