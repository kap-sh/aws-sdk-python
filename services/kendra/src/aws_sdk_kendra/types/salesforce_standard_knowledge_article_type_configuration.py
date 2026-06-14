"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceStandardKnowledgeArticleTypeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_field_name
    import aws_sdk_kendra.types.data_source_to_index_field_mapping_list


class SalesforceStandardKnowledgeArticleTypeConfiguration(TypedDict):
    document_data_field_name: (
        "aws_sdk_kendra.types.data_source_field_name.DataSourceFieldName"
    )
    """<p>The name of the field that contains the document data to index.</p>"""
    document_title_field_name: NotRequired[
        "aws_sdk_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The name of the field that contains the document title.</p>"""
    field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    r"""<p>Maps attributes or field names of the knowledge article to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Salesforce fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\">Mapping data source fields</a>. The Salesforce data source field names must exist in your Salesforce custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: SalesforceStandardKnowledgeArticleTypeConfiguration,
) -> dict:
    out: dict = {}
    out["DocumentDataFieldName"] = value["document_data_field_name"]
    if "document_title_field_name" in value:
        out["DocumentTitleFieldName"] = value["document_title_field_name"]
    if "field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> SalesforceStandardKnowledgeArticleTypeConfiguration:
    out: SalesforceStandardKnowledgeArticleTypeConfiguration = {}  # type: ignore[typeddict-item]
    if "DocumentDataFieldName" in data:
        out["document_data_field_name"] = data["DocumentDataFieldName"]
    else:
        raise DeserializationError(
            "SalesforceStandardKnowledgeArticleTypeConfiguration.document_data_field_name required"
        )
    if "DocumentTitleFieldName" in data:
        out["document_title_field_name"] = data["DocumentTitleFieldName"]
    if "FieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    return out
