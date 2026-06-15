"""Generated from Smithy shape ``com.amazonaws.kendra#JiraConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings
    import aws_sdk_kendra.types.data_source_to_index_field_mapping_list
    import aws_sdk_kendra.types.data_source_vpc_configuration
    import aws_sdk_kendra.types.issue_sub_entity_filter
    import aws_sdk_kendra.types.issue_type
    import aws_sdk_kendra.types.jira_account_url
    import aws_sdk_kendra.types.jira_status
    import aws_sdk_kendra.types.project
    import aws_sdk_kendra.types.secret_arn


class JiraConfiguration(TypedDict):
    jira_account_url: "aws_sdk_kendra.types.jira_account_url.JiraAccountUrl"
    """<p>The URL of the Jira account. For example, <i>company.atlassian.net</i>.</p>"""
    secret_arn: "aws_sdk_kendra.types.secret_arn.SecretArn"
    r"""<p>The Amazon Resource Name (ARN) of a secret in Secrets Manager contains the key-value pairs required to connect to your Jira data source. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>jiraId—The Jira user name or email.</p> </li> <li> <p>jiraCredentials—The Jira API token. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/data-source-jira.html\">Using a Jira data source</a>.</p> </li> </ul>"""
    use_change_log: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use the Jira change log to determine which documents require updating in the index. Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Jira.</p>"""
    project: NotRequired["aws_sdk_kendra.types.project.Project"]
    """<p>Specify which projects to crawl in your Jira data source. You can specify one or more Jira project IDs.</p>"""
    issue_type: NotRequired["aws_sdk_kendra.types.issue_type.IssueType"]
    """<p>Specify which issue types to crawl in your Jira data source. You can specify one or more of these options to crawl.</p>"""
    status: NotRequired["aws_sdk_kendra.types.jira_status.JiraStatus"]
    """<p>Specify which statuses to crawl in your Jira data source. You can specify one or more of these options to crawl.</p>"""
    issue_sub_entity_filter: NotRequired[
        "aws_sdk_kendra.types.issue_sub_entity_filter.IssueSubEntityFilter"
    ]
    """<p>Specify whether to crawl comments, attachments, and work logs. You can specify one or more of these options.</p>"""
    attachment_field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    r"""<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Jira attachments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Jira fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\"> Mapping data source fields</a>. The Jira data source field names must exist in your Jira custom metadata.</p>"""
    comment_field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    r"""<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Jira comments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Jira fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\"> Mapping data source fields</a>. The Jira data source field names must exist in your Jira custom metadata.</p>"""
    issue_field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    r"""<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Jira issues to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Jira fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\"> Mapping data source fields</a>. The Jira data source field names must exist in your Jira custom metadata.</p>"""
    project_field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    r"""<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Jira projects to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Jira fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\"> Mapping data source fields</a>. The Jira data source field names must exist in your Jira custom metadata.</p>"""
    work_log_field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    r"""<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Jira work logs to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Jira fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\"> Mapping data source fields</a>. The Jira data source field names must exist in your Jira custom metadata.</p>"""
    inclusion_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain file paths, file names, and file types in your Jira data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain file paths, file names, and file types in your Jira data source. Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    r"""<p>Configuration information for an Amazon Virtual Private Cloud to connect to your Jira. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html\">Configuring a VPC</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JiraConfiguration) -> dict:
    out: dict = {}
    out["JiraAccountUrl"] = value["jira_account_url"]
    out["SecretArn"] = value["secret_arn"]
    out["UseChangeLog"] = value.get("use_change_log", False)
    if "project" in value:
        import aws_sdk_kendra.types.project

        out["Project"] = aws_sdk_kendra.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    if "issue_type" in value:
        import aws_sdk_kendra.types.issue_type

        out["IssueType"] = aws_sdk_kendra.types.issue_type.serialize_aws_json_1_1(
            value["issue_type"]
        )
    if "status" in value:
        import aws_sdk_kendra.types.jira_status

        out["Status"] = aws_sdk_kendra.types.jira_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "issue_sub_entity_filter" in value:
        import aws_sdk_kendra.types.issue_sub_entity_filter

        out["IssueSubEntityFilter"] = (
            aws_sdk_kendra.types.issue_sub_entity_filter.serialize_aws_json_1_1(
                value["issue_sub_entity_filter"]
            )
        )
    if "attachment_field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["AttachmentFieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["attachment_field_mappings"]
            )
        )
    if "comment_field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["CommentFieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["comment_field_mappings"]
            )
        )
    if "issue_field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["IssueFieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["issue_field_mappings"]
            )
        )
    if "project_field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["ProjectFieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["project_field_mappings"]
            )
        )
    if "work_log_field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["WorkLogFieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["work_log_field_mappings"]
            )
        )
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
    if "vpc_configuration" in value:
        import aws_sdk_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            aws_sdk_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JiraConfiguration:
    out: JiraConfiguration = {}  # type: ignore[typeddict-item]
    if "JiraAccountUrl" in data:
        out["jira_account_url"] = data["JiraAccountUrl"]
    else:
        raise DeserializationError("JiraConfiguration.jira_account_url required")
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("JiraConfiguration.secret_arn required")
    if "UseChangeLog" in data:
        out["use_change_log"] = data["UseChangeLog"]
    else:
        out["use_change_log"] = False
    if "Project" in data:
        import aws_sdk_kendra.types.project

        out["project"] = aws_sdk_kendra.types.project.deserialize_aws_json_1_1(
            data["Project"]
        )
    if "IssueType" in data:
        import aws_sdk_kendra.types.issue_type

        out["issue_type"] = aws_sdk_kendra.types.issue_type.deserialize_aws_json_1_1(
            data["IssueType"]
        )
    if "Status" in data:
        import aws_sdk_kendra.types.jira_status

        out["status"] = aws_sdk_kendra.types.jira_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "IssueSubEntityFilter" in data:
        import aws_sdk_kendra.types.issue_sub_entity_filter

        out["issue_sub_entity_filter"] = (
            aws_sdk_kendra.types.issue_sub_entity_filter.deserialize_aws_json_1_1(
                data["IssueSubEntityFilter"]
            )
        )
    if "AttachmentFieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["attachment_field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["AttachmentFieldMappings"]
            )
        )
    if "CommentFieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["comment_field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["CommentFieldMappings"]
            )
        )
    if "IssueFieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["issue_field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["IssueFieldMappings"]
            )
        )
    if "ProjectFieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["project_field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["ProjectFieldMappings"]
            )
        )
    if "WorkLogFieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["work_log_field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["WorkLogFieldMappings"]
            )
        )
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
    if "VpcConfiguration" in data:
        import aws_sdk_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    return out
