"""Generated from Smithy shape ``com.amazonaws.kendra#ServiceNowServiceCatalogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.data_source_field_name
    import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings
    import aws_sdk_kendra.types.data_source_to_index_field_mapping_list


class ServiceNowServiceCatalogConfiguration(TypedDict):
    crawl_attachments: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index attachments to service catalog items.</p>"""
    include_attachment_file_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain attachments of catalogs in your ServiceNow. Item that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.</p> <p>The regex is applied to the file name of the attachment.</p>"""
    exclude_attachment_file_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain attachments of catalogs in your ServiceNow. Item that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.</p> <p>The regex is applied to the file name of the attachment.</p>"""
    document_data_field_name: (
        "aws_sdk_kendra.types.data_source_field_name.DataSourceFieldName"
    )
    """<p>The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.</p>"""
    document_title_field_name: NotRequired[
        "aws_sdk_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The name of the ServiceNow field that is mapped to the index document title field.</p>"""
    field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>Maps attributes or field names of catalogs to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to ServiceNow fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\">Mapping data source fields</a>. The ServiceNow data source field names must exist in your ServiceNow custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceNowServiceCatalogConfiguration) -> dict:
    out: dict = {}
    out["CrawlAttachments"] = value.get("crawl_attachments", False)
    if "include_attachment_file_patterns" in value:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["IncludeAttachmentFilePatterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["include_attachment_file_patterns"]
            )
        )
    if "exclude_attachment_file_patterns" in value:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["ExcludeAttachmentFilePatterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["exclude_attachment_file_patterns"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> ServiceNowServiceCatalogConfiguration:
    out: ServiceNowServiceCatalogConfiguration = {}  # type: ignore[typeddict-item]
    if "CrawlAttachments" in data:
        out["crawl_attachments"] = data["CrawlAttachments"]
    else:
        out["crawl_attachments"] = False
    if "IncludeAttachmentFilePatterns" in data:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["include_attachment_file_patterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["IncludeAttachmentFilePatterns"]
            )
        )
    if "ExcludeAttachmentFilePatterns" in data:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["exclude_attachment_file_patterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["ExcludeAttachmentFilePatterns"]
            )
        )
    if "DocumentDataFieldName" in data:
        out["document_data_field_name"] = data["DocumentDataFieldName"]
    else:
        raise DeserializationError(
            "ServiceNowServiceCatalogConfiguration.document_data_field_name required"
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
