"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketMetadataConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name


class GetBucketMetadataConfigurationRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that corresponds to the metadata configuration that you want to retrieve. </p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p> The expected owner of the general purpose bucket that you want to retrieve the metadata table configuration for. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketMetadataConfigurationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketMetadataConfigurationRequest:
    out: GetBucketMetadataConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
