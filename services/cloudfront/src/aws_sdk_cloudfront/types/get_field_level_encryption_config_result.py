"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_config
    import aws_sdk_cloudfront.types.string


class GetFieldLevelEncryptionConfigResult(TypedDict, closed=True):
    field_level_encryption_config: NotRequired[
        "aws_sdk_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig"
    ]
    """<p>Return the field-level encryption configuration information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the field level encryption configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption_config" in value:
        import aws_sdk_cloudfront.types.field_level_encryption_config

        aws_sdk_cloudfront.types.field_level_encryption_config.serialize_xml(
            value["field_level_encryption_config"], el, "FieldLevelEncryptionConfig"
        )


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionConfigResult:
    out: GetFieldLevelEncryptionConfigResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption_config = el.find("FieldLevelEncryptionConfig")
    if child_field_level_encryption_config is not None:
        import aws_sdk_cloudfront.types.field_level_encryption_config

        out["field_level_encryption_config"] = (
            aws_sdk_cloudfront.types.field_level_encryption_config.deserialize_xml(
                child_field_level_encryption_config
            )
        )
    return out
