"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption
    import capo_cloudfront.types.string


class GetFieldLevelEncryptionResult(TypedDict, closed=True):
    field_level_encryption: NotRequired[
        "capo_cloudfront.types.field_level_encryption.FieldLevelEncryption"
    ]
    """<p>Return the field-level encryption configuration information.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the field level encryption configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption" in value:
        import capo_cloudfront.types.field_level_encryption

        capo_cloudfront.types.field_level_encryption.serialize_xml(
            value["field_level_encryption"], el, "FieldLevelEncryption"
        )


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionResult:
    out: GetFieldLevelEncryptionResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption = el.find("FieldLevelEncryption")
    if child_field_level_encryption is not None:
        import capo_cloudfront.types.field_level_encryption

        out["field_level_encryption"] = (
            capo_cloudfront.types.field_level_encryption.deserialize_xml(
                child_field_level_encryption
            )
        )
    return out
