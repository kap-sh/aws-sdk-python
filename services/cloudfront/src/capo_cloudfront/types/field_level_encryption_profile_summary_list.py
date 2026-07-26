"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_profile_summary

FieldLevelEncryptionProfileSummaryList: TypeAlias = list[
    "capo_cloudfront.types.field_level_encryption_profile_summary.FieldLevelEncryptionProfileSummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionProfileSummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.field_level_encryption_profile_summary

        capo_cloudfront.types.field_level_encryption_profile_summary.serialize_xml(
            item, el, "FieldLevelEncryptionProfileSummary"
        )


def deserialize_xml(el: Element) -> FieldLevelEncryptionProfileSummaryList:
    import capo_cloudfront.types.field_level_encryption_profile_summary

    out: FieldLevelEncryptionProfileSummaryList = []
    for child in el.findall("FieldLevelEncryptionProfileSummary"):
        out.append(
            capo_cloudfront.types.field_level_encryption_profile_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: FieldLevelEncryptionProfileSummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.field_level_encryption_profile_summary

        capo_cloudfront.types.field_level_encryption_profile_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> FieldLevelEncryptionProfileSummaryList:
    import capo_cloudfront.types.field_level_encryption_profile_summary

    out: FieldLevelEncryptionProfileSummaryList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.field_level_encryption_profile_summary.deserialize_xml(
                child
            )
        )
    return out
