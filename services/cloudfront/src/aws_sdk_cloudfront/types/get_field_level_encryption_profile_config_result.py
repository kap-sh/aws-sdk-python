"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionProfileConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_profile_config
    import aws_sdk_cloudfront.types.string


class GetFieldLevelEncryptionProfileConfigResult(TypedDict):
    field_level_encryption_profile_config: NotRequired[
        "aws_sdk_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig"
    ]
    """<p>Return the field-level encryption profile configuration information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the field-level encryption profile configuration result. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionProfileConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption_profile_config" in value:
        import aws_sdk_cloudfront.types.field_level_encryption_profile_config

        aws_sdk_cloudfront.types.field_level_encryption_profile_config.serialize_xml(
            value["field_level_encryption_profile_config"],
            el,
            "FieldLevelEncryptionProfileConfig",
        )


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionProfileConfigResult:
    out: GetFieldLevelEncryptionProfileConfigResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption_profile_config = el.find(
        "FieldLevelEncryptionProfileConfig"
    )
    if child_field_level_encryption_profile_config is not None:
        import aws_sdk_cloudfront.types.field_level_encryption_profile_config

        out["field_level_encryption_profile_config"] = (
            aws_sdk_cloudfront.types.field_level_encryption_profile_config.deserialize_xml(
                child_field_level_encryption_profile_config
            )
        )
    return out
