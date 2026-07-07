"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListFieldLevelEncryptionConfigsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_list


class ListFieldLevelEncryptionConfigsResult(TypedDict, closed=True):
    field_level_encryption_list: NotRequired[
        "aws_sdk_cloudfront.types.field_level_encryption_list.FieldLevelEncryptionList"
    ]
    """<p>Returns a list of all field-level encryption configurations that have been created in CloudFront for this account.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListFieldLevelEncryptionConfigsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "field_level_encryption_list" in value:
        import aws_sdk_cloudfront.types.field_level_encryption_list

        aws_sdk_cloudfront.types.field_level_encryption_list.serialize_xml(
            value["field_level_encryption_list"], el, "FieldLevelEncryptionList"
        )


def deserialize_xml(el: Element) -> ListFieldLevelEncryptionConfigsResult:
    out: ListFieldLevelEncryptionConfigsResult = {}  # type: ignore[typeddict-item]
    child_field_level_encryption_list = el.find("FieldLevelEncryptionList")
    if child_field_level_encryption_list is not None:
        import aws_sdk_cloudfront.types.field_level_encryption_list

        out["field_level_encryption_list"] = (
            aws_sdk_cloudfront.types.field_level_encryption_list.deserialize_xml(
                child_field_level_encryption_list
            )
        )
    return out
