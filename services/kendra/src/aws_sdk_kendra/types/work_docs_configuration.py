"""Generated from Smithy shape ``com.amazonaws.kendra#WorkDocsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings
    import aws_sdk_kendra.types.data_source_to_index_field_mapping_list
    import aws_sdk_kendra.types.organization_id


class WorkDocsConfiguration(TypedDict):
    organization_id: "aws_sdk_kendra.types.organization_id.OrganizationId"
    """<p>The identifier of the directory corresponding to your WorkDocs site repository.</p> <p>You can find the organization ID in the <a href=\"https://console.aws.amazon.com/directoryservicev2/\">Directory Service</a> by going to <b>Active Directory</b>, then <b>Directories</b>. Your WorkDocs site directory has an ID, which is the organization ID. You can also set up a new WorkDocs directory in the Directory Service console and enable a WorkDocs site for the directory in the WorkDocs console.</p>"""
    crawl_comments: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to include comments on documents in your index. Including comments in your index means each comment is a document that can be searched on.</p> <p>The default is set to <code>FALSE</code>.</p>"""
    use_change_log: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use the WorkDocs change log to determine which documents require updating in the index. Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in WorkDocs.</p>"""
    inclusion_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain files in your WorkDocs site repository. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain files in your WorkDocs site repository. Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map WorkDocs data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to WorkDocs fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\">Mapping data source fields</a>. The WorkDocs data source field names must exist in your WorkDocs custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkDocsConfiguration) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["CrawlComments"] = value.get("crawl_comments", False)
    out["UseChangeLog"] = value.get("use_change_log", False)
    if "inclusion_patterns" in value:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["InclusionPatterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["inclusion_patterns"]
            )
        )
    if "exclusion_patterns" in value:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["ExclusionPatterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["exclusion_patterns"]
            )
        )
    if "field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkDocsConfiguration:
    out: WorkDocsConfiguration = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("WorkDocsConfiguration.organization_id required")
    if "CrawlComments" in data:
        out["crawl_comments"] = data["CrawlComments"]
    else:
        out["crawl_comments"] = False
    if "UseChangeLog" in data:
        out["use_change_log"] = data["UseChangeLog"]
    else:
        out["use_change_log"] = False
    if "InclusionPatterns" in data:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["inclusion_patterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["InclusionPatterns"]
            )
        )
    if "ExclusionPatterns" in data:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["exclusion_patterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["ExclusionPatterns"]
            )
        )
    if "FieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    return out
