"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_profile_summary

FieldLevelEncryptionProfileSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.field_level_encryption_profile_summary.FieldLevelEncryptionProfileSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionProfileSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.field_level_encryption_profile_summary

        aws_sdk_cloudfront.types.field_level_encryption_profile_summary.serialize_xml(
            item, el, "FieldLevelEncryptionProfileSummary"
        )


def deserialize_xml(el: Element) -> FieldLevelEncryptionProfileSummaryList:
    import aws_sdk_cloudfront.types.field_level_encryption_profile_summary

    out: FieldLevelEncryptionProfileSummaryList = []
    for child in el.findall("FieldLevelEncryptionProfileSummary"):
        out.append(
            aws_sdk_cloudfront.types.field_level_encryption_profile_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: FieldLevelEncryptionProfileSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.field_level_encryption_profile_summary

        aws_sdk_cloudfront.types.field_level_encryption_profile_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> FieldLevelEncryptionProfileSummaryList:
    import aws_sdk_cloudfront.types.field_level_encryption_profile_summary

    out: FieldLevelEncryptionProfileSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.field_level_encryption_profile_summary.deserialize_xml(
                child
            )
        )
    return out
