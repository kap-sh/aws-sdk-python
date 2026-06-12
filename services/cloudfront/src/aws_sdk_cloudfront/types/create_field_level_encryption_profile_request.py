"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFieldLevelEncryptionProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_profile_config


class CreateFieldLevelEncryptionProfileRequest(TypedDict):
    field_level_encryption_profile_config: "aws_sdk_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig"
    """<p>The request to create a field-level encryption profile.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateFieldLevelEncryptionProfileRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.field_level_encryption_profile_config

    aws_sdk_cloudfront.types.field_level_encryption_profile_config.serialize_xml(
        value["field_level_encryption_profile_config"],
        el,
        "FieldLevelEncryptionProfileConfig",
    )


def deserialize_xml(el: Element) -> CreateFieldLevelEncryptionProfileRequest:
    out: CreateFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
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
            "CreateFieldLevelEncryptionProfileRequest.field_level_encryption_profile_config required"
        )
    return out
