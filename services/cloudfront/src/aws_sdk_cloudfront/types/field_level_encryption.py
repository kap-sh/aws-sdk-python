"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_config
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class FieldLevelEncryption(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.</p>"""
    last_modified_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The last time the field-level encryption configuration was changed.</p>"""
    field_level_encryption_config: "aws_sdk_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig"
    """<p>A complex data type that includes the profile configurations specified for field-level encryption.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FieldLevelEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import aws_sdk_cloudfront.types.field_level_encryption_config

    aws_sdk_cloudfront.types.field_level_encryption_config.serialize_xml(
        value["field_level_encryption_config"], el, "FieldLevelEncryptionConfig"
    )


def deserialize_xml(el: Element) -> FieldLevelEncryption:
    out: FieldLevelEncryption = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("FieldLevelEncryption.id required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["last_modified_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("FieldLevelEncryption.last_modified_time required")
    child_field_level_encryption_config = el.find("FieldLevelEncryptionConfig")
    if child_field_level_encryption_config is not None:
        import aws_sdk_cloudfront.types.field_level_encryption_config

        out["field_level_encryption_config"] = (
            aws_sdk_cloudfront.types.field_level_encryption_config.deserialize_xml(
                child_field_level_encryption_config
            )
        )
    else:
        raise DeserializationError(
            "FieldLevelEncryption.field_level_encryption_config required"
        )
    return out
