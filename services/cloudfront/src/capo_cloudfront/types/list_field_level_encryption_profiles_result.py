"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListFieldLevelEncryptionProfilesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_profile_list


class ListFieldLevelEncryptionProfilesResult(TypedDict, closed=True):
    field_level_encryption_profile_list: NotRequired[
        "capo_cloudfront.types.field_level_encryption_profile_list.FieldLevelEncryptionProfileList"
    ]
    """<p>Returns a list of the field-level encryption profiles that have been created in CloudFront for this account.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListFieldLevelEncryptionProfilesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption_profile_list" in value:
        import capo_cloudfront.types.field_level_encryption_profile_list

        capo_cloudfront.types.field_level_encryption_profile_list.serialize_xml(
            value["field_level_encryption_profile_list"],
            el,
            "FieldLevelEncryptionProfileList",
        )


def deserialize_xml(el: Element) -> ListFieldLevelEncryptionProfilesResult:
    out: ListFieldLevelEncryptionProfilesResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption_profile_list = el.find(
        "FieldLevelEncryptionProfileList"
    )
    if child_field_level_encryption_profile_list is not None:
        import capo_cloudfront.types.field_level_encryption_profile_list

        out["field_level_encryption_profile_list"] = (
            capo_cloudfront.types.field_level_encryption_profile_list.deserialize_xml(
                child_field_level_encryption_profile_list
            )
        )
    return out
