"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateFieldLevelEncryptionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_config
    import capo_cloudfront.types.string


class UpdateFieldLevelEncryptionConfigRequest(TypedDict, closed=True):
    field_level_encryption_config: (
        "capo_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig"
    )
    """<p>Request to update a field-level encryption configuration.</p>"""
    id: "capo_cloudfront.types.string.string"
    """<p>The ID of the configuration you want to update.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the configuration identity to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateFieldLevelEncryptionConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.field_level_encryption_config

    capo_cloudfront.types.field_level_encryption_config.serialize_xml(
        value["field_level_encryption_config"], el, "FieldLevelEncryptionConfig"
    )


def deserialize_xml(el: Element) -> UpdateFieldLevelEncryptionConfigRequest:
    out: UpdateFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
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
            "UpdateFieldLevelEncryptionConfigRequest.field_level_encryption_config required"
        )
    return out
