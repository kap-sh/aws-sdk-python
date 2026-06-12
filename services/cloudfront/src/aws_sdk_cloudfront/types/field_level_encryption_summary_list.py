"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_level_encryption_summary

FieldLevelEncryptionSummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.field_level_encryption_summary.FieldLevelEncryptionSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.field_level_encryption_summary

        aws_sdk_cloudfront.types.field_level_encryption_summary.serialize_xml(
            item, el, "FieldLevelEncryptionSummary"
        )


def deserialize_xml(el: Element) -> FieldLevelEncryptionSummaryList:
    import aws_sdk_cloudfront.types.field_level_encryption_summary

    out: FieldLevelEncryptionSummaryList = []
    for child in el.findall("FieldLevelEncryptionSummary"):
        out.append(
            aws_sdk_cloudfront.types.field_level_encryption_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: FieldLevelEncryptionSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.field_level_encryption_summary

        aws_sdk_cloudfront.types.field_level_encryption_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> FieldLevelEncryptionSummaryList:
    import aws_sdk_cloudfront.types.field_level_encryption_summary

    out: FieldLevelEncryptionSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.field_level_encryption_summary.deserialize_xml(
                child
            )
        )
    return out
