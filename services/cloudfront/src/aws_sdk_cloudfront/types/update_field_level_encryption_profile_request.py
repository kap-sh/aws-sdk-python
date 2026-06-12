"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateFieldLevelEncryptionProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_profile_config
    import aws_sdk_cloudfront.types.string


class UpdateFieldLevelEncryptionProfileRequest(TypedDict):
    field_level_encryption_profile_config: "aws_sdk_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig"
    """<p>Request to update a field-level encryption profile.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the field-level encryption profile request.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the profile identity to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateFieldLevelEncryptionProfileRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.field_level_encryption_profile_config

    aws_sdk_cloudfront.types.field_level_encryption_profile_config.serialize_xml(
        value["field_level_encryption_profile_config"],
        el,
        "FieldLevelEncryptionProfileConfig",
    )


def deserialize_xml(el: Element) -> UpdateFieldLevelEncryptionProfileRequest:
    out: UpdateFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError(
            "UpdateFieldLevelEncryptionProfileRequest.field_level_encryption_profile_config required"
        )
    return out
