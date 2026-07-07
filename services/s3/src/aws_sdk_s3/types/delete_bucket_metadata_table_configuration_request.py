"""Generated from Smithy shape ``com.amazonaws.s3#DeleteBucketMetadataTableConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name


class DeleteBucketMetadataTableConfigurationRequest(TypedDict, closed=True):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that you want to remove the metadata table configuration from. </p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p> The expected bucket owner of the general purpose bucket that you want to remove the metadata table configuration from. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteBucketMetadataTableConfigurationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteBucketMetadataTableConfigurationRequest:
    out: DeleteBucketMetadataTableConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
