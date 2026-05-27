"""Generated from Smithy shape ``com.amazonaws.s3#CreateBucketMetadataConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.checksum_algorithm
    import aws_sdk_s3.types.content_md5
    import aws_sdk_s3.types.metadata_configuration


class CreateBucketMetadataConfigurationRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that you want to create the metadata configuration for. </p>"""
    content_md5: NotRequired["aws_sdk_s3.types.content_md5.ContentMD5"]
    """<p> The <code>Content-MD5</code> header for the metadata configuration. </p>"""
    checksum_algorithm: NotRequired[
        "aws_sdk_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p> The checksum algorithm to use with your metadata configuration. </p>"""
    metadata_configuration: (
        "aws_sdk_s3.types.metadata_configuration.MetadataConfiguration"
    )
    """<p> The contents of your metadata configuration. </p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p> The expected owner of the general purpose bucket that corresponds to your metadata configuration. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateBucketMetadataConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.metadata_configuration

    aws_sdk_s3.types.metadata_configuration.serialize_xml(
        value["metadata_configuration"], el, "MetadataConfiguration"
    )


def deserialize_xml(el: Element) -> CreateBucketMetadataConfigurationRequest:
    out: CreateBucketMetadataConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_metadata_configuration = el.find("MetadataConfiguration")
    if child_metadata_configuration is not None:
        import aws_sdk_s3.types.metadata_configuration

        out["metadata_configuration"] = (
            aws_sdk_s3.types.metadata_configuration.deserialize_xml(
                child_metadata_configuration
            )
        )
    else:
        raise DeserializationError(
            "CreateBucketMetadataConfigurationRequest.metadata_configuration required"
        )
    return out
