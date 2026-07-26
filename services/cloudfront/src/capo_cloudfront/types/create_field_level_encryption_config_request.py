"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFieldLevelEncryptionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_config


class CreateFieldLevelEncryptionConfigRequest(TypedDict, closed=True):
    field_level_encryption_config: (
        "capo_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig"
    )
    """<p>The request to create a new field-level encryption configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateFieldLevelEncryptionConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.field_level_encryption_config

    capo_cloudfront.types.field_level_encryption_config.serialize_xml(
        value["field_level_encryption_config"], el, "FieldLevelEncryptionConfig"
    )


def deserialize_xml(el: Element) -> CreateFieldLevelEncryptionConfigRequest:
    out: CreateFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
    child_field_level_encryption_config = el.find("FieldLevelEncryptionConfig")
    if child_field_level_encryption_config is not None:
        import capo_cloudfront.types.field_level_encryption_config

        out["field_level_encryption_config"] = (
            capo_cloudfront.types.field_level_encryption_config.deserialize_xml(
                child_field_level_encryption_config
            )
        )
    else:
        raise DeserializationError(
            "CreateFieldLevelEncryptionConfigRequest.field_level_encryption_config required"
        )
    return out
