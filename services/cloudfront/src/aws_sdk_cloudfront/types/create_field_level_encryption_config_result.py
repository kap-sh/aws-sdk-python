"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFieldLevelEncryptionConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption
    import aws_sdk_cloudfront.types.string


class CreateFieldLevelEncryptionConfigResult(TypedDict, closed=True):
    field_level_encryption: NotRequired[
        "aws_sdk_cloudfront.types.field_level_encryption.FieldLevelEncryption"
    ]
    """<p>Returned when you create a new field-level encryption configuration.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the new configuration resource just created.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the field level encryption configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateFieldLevelEncryptionConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption" in value:
        import aws_sdk_cloudfront.types.field_level_encryption

        aws_sdk_cloudfront.types.field_level_encryption.serialize_xml(
            value["field_level_encryption"], el, "FieldLevelEncryption"
        )


def deserialize_xml(el: Element) -> CreateFieldLevelEncryptionConfigResult:
    out: CreateFieldLevelEncryptionConfigResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption = el.find("FieldLevelEncryption")
    if child_field_level_encryption is not None:
        import aws_sdk_cloudfront.types.field_level_encryption

        out["field_level_encryption"] = (
            aws_sdk_cloudfront.types.field_level_encryption.deserialize_xml(
                child_field_level_encryption
            )
        )
    return out
