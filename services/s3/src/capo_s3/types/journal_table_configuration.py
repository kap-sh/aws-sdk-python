"""Generated from Smithy shape ``com.amazonaws.s3#JournalTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.metadata_table_encryption_configuration
    import capo_s3.types.record_expiration


class JournalTableConfiguration(TypedDict, closed=True):
    record_expiration: "capo_s3.types.record_expiration.RecordExpiration"
    """<p> The journal table record expiration settings for the journal table. </p>"""
    encryption_configuration: NotRequired[
        "capo_s3.types.metadata_table_encryption_configuration.MetadataTableEncryptionConfiguration"
    ]
    """<p> The encryption configuration for the journal table. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: JournalTableConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.record_expiration

    capo_s3.types.record_expiration.serialize_xml(
        value["record_expiration"], el, "RecordExpiration"
    )
    if "encryption_configuration" in value:
        import capo_s3.types.metadata_table_encryption_configuration

        capo_s3.types.metadata_table_encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )


def deserialize_xml(el: Element) -> JournalTableConfiguration:
    out: JournalTableConfiguration = {}  # type: ignore[typeddict-item]
    child_record_expiration = el.find("RecordExpiration")
    if child_record_expiration is not None:
        import capo_s3.types.record_expiration

        out["record_expiration"] = capo_s3.types.record_expiration.deserialize_xml(
            child_record_expiration
        )
    else:
        raise DeserializationError(
            "JournalTableConfiguration.record_expiration required"
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import capo_s3.types.metadata_table_encryption_configuration

        out["encryption_configuration"] = (
            capo_s3.types.metadata_table_encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    return out
