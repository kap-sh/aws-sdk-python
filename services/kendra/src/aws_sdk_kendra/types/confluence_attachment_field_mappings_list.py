"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAttachmentFieldMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.confluence_attachment_to_index_field_mapping

ConfluenceAttachmentFieldMappingsList: TypeAlias = list[
    "aws_sdk_kendra.types.confluence_attachment_to_index_field_mapping.ConfluenceAttachmentToIndexFieldMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceAttachmentFieldMappingsList) -> list:
    import aws_sdk_kendra.types.confluence_attachment_to_index_field_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.confluence_attachment_to_index_field_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfluenceAttachmentFieldMappingsList:
    import aws_sdk_kendra.types.confluence_attachment_to_index_field_mapping

    out: ConfluenceAttachmentFieldMappingsList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.confluence_attachment_to_index_field_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
