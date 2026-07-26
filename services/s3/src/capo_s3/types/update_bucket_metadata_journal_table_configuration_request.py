"""Generated from Smithy shape ``com.amazonaws.s3#UpdateBucketMetadataJournalTableConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.journal_table_configuration_updates


class UpdateBucketMetadataJournalTableConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that corresponds to the metadata configuration that you want to enable or disable journal table record expiration for. </p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p> The <code>Content-MD5</code> header for the journal table configuration. </p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p> The checksum algorithm to use with your journal table configuration. </p>"""
    journal_table_configuration: "capo_s3.types.journal_table_configuration_updates.JournalTableConfigurationUpdates"
    """<p> The contents of your journal table configuration. </p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p> The expected owner of the general purpose bucket that corresponds to the metadata table configuration that you want to enable or disable journal table record expiration for. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateBucketMetadataJournalTableConfigurationRequest,
    parent: Element,
    tag: str,
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.journal_table_configuration_updates

    capo_s3.types.journal_table_configuration_updates.serialize_xml(
        value["journal_table_configuration"], el, "JournalTableConfiguration"
    )


def deserialize_xml(
    el: Element,
) -> UpdateBucketMetadataJournalTableConfigurationRequest:
    out: UpdateBucketMetadataJournalTableConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_journal_table_configuration = el.find("JournalTableConfiguration")
    if child_journal_table_configuration is not None:
        import capo_s3.types.journal_table_configuration_updates

        out["journal_table_configuration"] = (
            capo_s3.types.journal_table_configuration_updates.deserialize_xml(
                child_journal_table_configuration
            )
        )
    else:
        raise DeserializationError(
            "UpdateBucketMetadataJournalTableConfigurationRequest.journal_table_configuration required"
        )
    return out
