"""Generated from Smithy shape ``com.amazonaws.s3#UpdateBucketMetadataAnnotationTableConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.annotation_table_configuration_updates
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5


class UpdateBucketMetadataAnnotationTableConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket whose annotation table configuration to update.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>Base64-encoded MD5 digest of the message body.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Checksum algorithm for the request payload.</p>"""
    annotation_table_configuration: "capo_s3.types.annotation_table_configuration_updates.AnnotationTableConfigurationUpdates"
    """<p>The annotation table configuration updates to apply.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateBucketMetadataAnnotationTableConfigurationRequest,
    parent: Element,
    tag: str,
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.annotation_table_configuration_updates

    capo_s3.types.annotation_table_configuration_updates.serialize_xml(
        value["annotation_table_configuration"], el, "AnnotationTableConfiguration"
    )


def deserialize_xml(
    el: Element,
) -> UpdateBucketMetadataAnnotationTableConfigurationRequest:
    out: UpdateBucketMetadataAnnotationTableConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_annotation_table_configuration = el.find("AnnotationTableConfiguration")
    if child_annotation_table_configuration is not None:
        import capo_s3.types.annotation_table_configuration_updates

        out["annotation_table_configuration"] = (
            capo_s3.types.annotation_table_configuration_updates.deserialize_xml(
                child_annotation_table_configuration
            )
        )
    else:
        raise DeserializationError(
            "UpdateBucketMetadataAnnotationTableConfigurationRequest.annotation_table_configuration required"
        )
    return out
