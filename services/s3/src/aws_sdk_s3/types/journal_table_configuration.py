"""Generated from Smithy shape ``com.amazonaws.s3#JournalTableConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.metadata_table_encryption_configuration
    import aws_sdk_s3.types.record_expiration


class JournalTableConfiguration(TypedDict):
    record_expiration: "aws_sdk_s3.types.record_expiration.RecordExpiration"
    """<p> The journal table record expiration settings for the journal table. </p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_s3.types.metadata_table_encryption_configuration.MetadataTableEncryptionConfiguration"
    ]
    """<p> The encryption configuration for the journal table. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: JournalTableConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.record_expiration

    aws_sdk_s3.types.record_expiration.serialize_xml(
        value["record_expiration"], el, "RecordExpiration"
    )
    if "encryption_configuration" in value:
        import aws_sdk_s3.types.metadata_table_encryption_configuration

        aws_sdk_s3.types.metadata_table_encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )


def deserialize_xml(el: Element) -> JournalTableConfiguration:
    out: JournalTableConfiguration = {}  # type: ignore[typeddict-item]
    child_record_expiration = el.find("RecordExpiration")
    if child_record_expiration is not None:
        import aws_sdk_s3.types.record_expiration

        out["record_expiration"] = aws_sdk_s3.types.record_expiration.deserialize_xml(
            child_record_expiration
        )
    else:
        raise DeserializationError(
            "JournalTableConfiguration.record_expiration required"
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import aws_sdk_s3.types.metadata_table_encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_s3.types.metadata_table_encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    return out
