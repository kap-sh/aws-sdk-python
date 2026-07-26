"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceBlogFieldMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.confluence_blog_to_index_field_mapping

ConfluenceBlogFieldMappingsList: TypeAlias = list[
    "capo_kendra.types.confluence_blog_to_index_field_mapping.ConfluenceBlogToIndexFieldMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceBlogFieldMappingsList) -> list:
    import capo_kendra.types.confluence_blog_to_index_field_mapping

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.confluence_blog_to_index_field_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfluenceBlogFieldMappingsList:
    import capo_kendra.types.confluence_blog_to_index_field_mapping

    out: ConfluenceBlogFieldMappingsList = []
    for item in data:
        out.append(
            capo_kendra.types.confluence_blog_to_index_field_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
