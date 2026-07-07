"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings
    import aws_sdk_kendra.types.salesforce_chatter_feed_configuration
    import aws_sdk_kendra.types.salesforce_knowledge_article_configuration
    import aws_sdk_kendra.types.salesforce_standard_object_attachment_configuration
    import aws_sdk_kendra.types.salesforce_standard_object_configuration_list
    import aws_sdk_kendra.types.secret_arn
    import aws_sdk_kendra.types.url


class SalesforceConfiguration(TypedDict, closed=True):
    server_url: "aws_sdk_kendra.types.url.Url"
    """<p>The instance URL for the Salesforce site that you want to index.</p>"""
    secret_arn: "aws_sdk_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Managersecret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token. </p> </li> <li> <p>consumerKey - The application public key generated when you created your Salesforce application.</p> </li> <li> <p>consumerSecret - The application private key generated when you created your Salesforce application.</p> </li> <li> <p>password - The password associated with the user logging in to the Salesforce instance.</p> </li> <li> <p>securityToken - The token associated with the user logging in to the Salesforce instance.</p> </li> <li> <p>username - The user name of the user logging in to the Salesforce instance.</p> </li> </ul>"""
    standard_object_configurations: NotRequired[
        "aws_sdk_kendra.types.salesforce_standard_object_configuration_list.SalesforceStandardObjectConfigurationList"
    ]
    """<p>Configuration of the Salesforce standard objects that Amazon Kendra indexes.</p>"""
    knowledge_article_configuration: NotRequired[
        "aws_sdk_kendra.types.salesforce_knowledge_article_configuration.SalesforceKnowledgeArticleConfiguration"
    ]
    """<p>Configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.</p>"""
    chatter_feed_configuration: NotRequired[
        "aws_sdk_kendra.types.salesforce_chatter_feed_configuration.SalesforceChatterFeedConfiguration"
    ]
    """<p>Configuration information for Salesforce chatter feeds.</p>"""
    crawl_attachments: "aws_sdk_kendra.types.boolean.Boolean"
    """<p>Indicates whether Amazon Kendra should index attachments to Salesforce objects.</p>"""
    standard_object_attachment_configuration: NotRequired[
        "aws_sdk_kendra.types.salesforce_standard_object_attachment_configuration.SalesforceStandardObjectAttachmentConfiguration"
    ]
    """<p>Configuration information for processing attachments to Salesforce standard objects. </p>"""
    include_attachment_file_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain documents in your Salesforce. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the name of the attached file.</p>"""
    exclude_attachment_file_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain documents in your Salesforce. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the name of the attached file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceConfiguration) -> dict:
    out: dict = {}
    out["ServerUrl"] = value["server_url"]
    out["SecretArn"] = value["secret_arn"]
    if "standard_object_configurations" in value:
        import aws_sdk_kendra.types.salesforce_standard_object_configuration_list

        out["StandardObjectConfigurations"] = (
            aws_sdk_kendra.types.salesforce_standard_object_configuration_list.serialize_aws_json_1_1(
                value["standard_object_configurations"]
            )
        )
    if "knowledge_article_configuration" in value:
        import aws_sdk_kendra.types.salesforce_knowledge_article_configuration

        out["KnowledgeArticleConfiguration"] = (
            aws_sdk_kendra.types.salesforce_knowledge_article_configuration.serialize_aws_json_1_1(
                value["knowledge_article_configuration"]
            )
        )
    if "chatter_feed_configuration" in value:
        import aws_sdk_kendra.types.salesforce_chatter_feed_configuration

        out["ChatterFeedConfiguration"] = (
            aws_sdk_kendra.types.salesforce_chatter_feed_configuration.serialize_aws_json_1_1(
                value["chatter_feed_configuration"]
            )
        )
    out["CrawlAttachments"] = value.get("crawl_attachments", False)
    if "standard_object_attachment_configuration" in value:
        import aws_sdk_kendra.types.salesforce_standard_object_attachment_configuration

        out["StandardObjectAttachmentConfiguration"] = (
            aws_sdk_kendra.types.salesforce_standard_object_attachment_configuration.serialize_aws_json_1_1(
                value["standard_object_attachment_configuration"]
            )
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> SalesforceConfiguration:
    out: SalesforceConfiguration = {}  # type: ignore[typeddict-item]
    if "ServerUrl" in data:
        out["server_url"] = data["ServerUrl"]
    else:
        raise DeserializationError("SalesforceConfiguration.server_url required")
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("SalesforceConfiguration.secret_arn required")
    if "StandardObjectConfigurations" in data:
        import aws_sdk_kendra.types.salesforce_standard_object_configuration_list

        out["standard_object_configurations"] = (
            aws_sdk_kendra.types.salesforce_standard_object_configuration_list.deserialize_aws_json_1_1(
                data["StandardObjectConfigurations"]
            )
        )
    if "KnowledgeArticleConfiguration" in data:
        import aws_sdk_kendra.types.salesforce_knowledge_article_configuration

        out["knowledge_article_configuration"] = (
            aws_sdk_kendra.types.salesforce_knowledge_article_configuration.deserialize_aws_json_1_1(
                data["KnowledgeArticleConfiguration"]
            )
        )
    if "ChatterFeedConfiguration" in data:
        import aws_sdk_kendra.types.salesforce_chatter_feed_configuration

        out["chatter_feed_configuration"] = (
            aws_sdk_kendra.types.salesforce_chatter_feed_configuration.deserialize_aws_json_1_1(
                data["ChatterFeedConfiguration"]
            )
        )
    if "CrawlAttachments" in data:
        out["crawl_attachments"] = data["CrawlAttachments"]
    else:
        out["crawl_attachments"] = False
    if "StandardObjectAttachmentConfiguration" in data:
        import aws_sdk_kendra.types.salesforce_standard_object_attachment_configuration

        out["standard_object_attachment_configuration"] = (
            aws_sdk_kendra.types.salesforce_standard_object_attachment_configuration.deserialize_aws_json_1_1(
                data["StandardObjectAttachmentConfiguration"]
            )
        )
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
    return out
