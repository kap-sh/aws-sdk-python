"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAttachmentFieldMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.confluence_attachment_to_index_field_mapping

ConfluenceAttachmentFieldMappingsList: TypeAlias = list[
    "capo_kendra.types.confluence_attachment_to_index_field_mapping.ConfluenceAttachmentToIndexFieldMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceAttachmentFieldMappingsList) -> list:
    import capo_kendra.types.confluence_attachment_to_index_field_mapping

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.confluence_attachment_to_index_field_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfluenceAttachmentFieldMappingsList:
    import capo_kendra.types.confluence_attachment_to_index_field_mapping

    out: ConfluenceAttachmentFieldMappingsList = []
    for item in data:
        out.append(
            capo_kendra.types.confluence_attachment_to_index_field_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
