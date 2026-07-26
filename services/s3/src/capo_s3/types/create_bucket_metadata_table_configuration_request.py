"""Generated from Smithy shape ``com.amazonaws.s3#CreateBucketMetadataTableConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.metadata_table_configuration


class CreateBucketMetadataTableConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that you want to create the metadata table configuration for. </p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p> The <code>Content-MD5</code> header for the metadata table configuration. </p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p> The checksum algorithm to use with your metadata table configuration. </p>"""
    metadata_table_configuration: (
        "capo_s3.types.metadata_table_configuration.MetadataTableConfiguration"
    )
    """<p> The contents of your metadata table configuration. </p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p> The expected owner of the general purpose bucket that corresponds to your metadata table configuration. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateBucketMetadataTableConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.metadata_table_configuration

    capo_s3.types.metadata_table_configuration.serialize_xml(
        value["metadata_table_configuration"], el, "MetadataTableConfiguration"
    )


def deserialize_xml(el: Element) -> CreateBucketMetadataTableConfigurationRequest:
    out: CreateBucketMetadataTableConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_metadata_table_configuration = el.find("MetadataTableConfiguration")
    if child_metadata_table_configuration is not None:
        import capo_s3.types.metadata_table_configuration

        out["metadata_table_configuration"] = (
            capo_s3.types.metadata_table_configuration.deserialize_xml(
                child_metadata_table_configuration
            )
        )
    else:
        raise DeserializationError(
            "CreateBucketMetadataTableConfigurationRequest.metadata_table_configuration required"
        )
    return out
