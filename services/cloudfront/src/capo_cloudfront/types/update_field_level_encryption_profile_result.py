"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateFieldLevelEncryptionProfileResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_profile
    import capo_cloudfront.types.string


class UpdateFieldLevelEncryptionProfileResult(TypedDict, closed=True):
    field_level_encryption_profile: NotRequired[
        "capo_cloudfront.types.field_level_encryption_profile.FieldLevelEncryptionProfile"
    ]
    """<p>Return the results of updating the profile.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The result of the field-level encryption profile request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateFieldLevelEncryptionProfileResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption_profile" in value:
        import capo_cloudfront.types.field_level_encryption_profile

        capo_cloudfront.types.field_level_encryption_profile.serialize_xml(
            value["field_level_encryption_profile"], el, "FieldLevelEncryptionProfile"
        )


def deserialize_xml(el: Element) -> UpdateFieldLevelEncryptionProfileResult:
    out: UpdateFieldLevelEncryptionProfileResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption_profile = el.find("FieldLevelEncryptionProfile")
    if child_field_level_encryption_profile is not None:
        import capo_cloudfront.types.field_level_encryption_profile

        out["field_level_encryption_profile"] = (
            capo_cloudfront.types.field_level_encryption_profile.deserialize_xml(
                child_field_level_encryption_profile
            )
        )
    return out
