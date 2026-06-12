"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluencePageFieldMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.confluence_page_to_index_field_mapping

ConfluencePageFieldMappingsList: TypeAlias = list[
    "aws_sdk_kendra.types.confluence_page_to_index_field_mapping.ConfluencePageToIndexFieldMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluencePageFieldMappingsList) -> list:
    import aws_sdk_kendra.types.confluence_page_to_index_field_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.confluence_page_to_index_field_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfluencePageFieldMappingsList:
    import aws_sdk_kendra.types.confluence_page_to_index_field_mapping

    out: ConfluencePageFieldMappingsList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.confluence_page_to_index_field_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
