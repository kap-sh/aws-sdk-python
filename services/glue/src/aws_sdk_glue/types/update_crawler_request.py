"""Generated from Smithy shape ``com.amazonaws.glue#UpdateCrawlerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.classifier_name_list
    import aws_sdk_glue.types.crawler_configuration
    import aws_sdk_glue.types.crawler_security_configuration
    import aws_sdk_glue.types.crawler_targets
    import aws_sdk_glue.types.cron_expression
    import aws_sdk_glue.types.database_name
    import aws_sdk_glue.types.description_string_removable
    import aws_sdk_glue.types.lake_formation_configuration
    import aws_sdk_glue.types.lineage_configuration
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.recrawl_policy
    import aws_sdk_glue.types.role
    import aws_sdk_glue.types.schema_change_policy
    import aws_sdk_glue.types.table_prefix


class UpdateCrawlerRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the new crawler.</p>"""
    role: NotRequired["aws_sdk_glue.types.role.Role"]
    """<p>The IAM role or Amazon Resource Name (ARN) of an IAM role that is used by the new crawler to access customer resources.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.database_name.DatabaseName"]
    """<p>The Glue database where results are stored, such as: <code>arn:aws:daylight:us-east-1::database/sometable/*</code>.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.description_string_removable.DescriptionStringRemovable"
    ]
    """<p>A description of the new crawler.</p>"""
    targets: NotRequired["aws_sdk_glue.types.crawler_targets.CrawlerTargets"]
    """<p>A list of targets to crawl.</p>"""
    schedule: NotRequired["aws_sdk_glue.types.cron_expression.CronExpression"]
    r"""<p>A <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>"""
    classifiers: NotRequired[
        "aws_sdk_glue.types.classifier_name_list.ClassifierNameList"
    ]
    """<p>A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.</p>"""
    table_prefix: NotRequired["aws_sdk_glue.types.table_prefix.TablePrefix"]
    """<p>The table prefix used for catalog tables that are created.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.schema_change_policy.SchemaChangePolicy"
    ]
    """<p>The policy for the crawler's update and deletion behavior.</p>"""
    recrawl_policy: NotRequired["aws_sdk_glue.types.recrawl_policy.RecrawlPolicy"]
    """<p>A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.</p>"""
    lineage_configuration: NotRequired[
        "aws_sdk_glue.types.lineage_configuration.LineageConfiguration"
    ]
    """<p>Specifies data lineage configuration settings for the crawler.</p>"""
    lake_formation_configuration: NotRequired[
        "aws_sdk_glue.types.lake_formation_configuration.LakeFormationConfiguration"
    ]
    """<p>Specifies Lake Formation configuration settings for the crawler.</p>"""
    configuration: NotRequired[
        "aws_sdk_glue.types.crawler_configuration.CrawlerConfiguration"
    ]
    r"""<p>Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html\">Setting crawler configuration options</a>.</p>"""
    crawler_security_configuration: NotRequired[
        "aws_sdk_glue.types.crawler_security_configuration.CrawlerSecurityConfiguration"
    ]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used by this crawler.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCrawlerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "role" in value:
        out["Role"] = value["role"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "targets" in value:
        import aws_sdk_glue.types.crawler_targets

        out["Targets"] = aws_sdk_glue.types.crawler_targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "classifiers" in value:
        import aws_sdk_glue.types.classifier_name_list

        out["Classifiers"] = (
            aws_sdk_glue.types.classifier_name_list.serialize_aws_json_1_1(
                value["classifiers"]
            )
        )
    if "table_prefix" in value:
        out["TablePrefix"] = value["table_prefix"]
    if "schema_change_policy" in value:
        import aws_sdk_glue.types.schema_change_policy

        out["SchemaChangePolicy"] = (
            aws_sdk_glue.types.schema_change_policy.serialize_aws_json_1_1(
                value["schema_change_policy"]
            )
        )
    if "recrawl_policy" in value:
        import aws_sdk_glue.types.recrawl_policy

        out["RecrawlPolicy"] = aws_sdk_glue.types.recrawl_policy.serialize_aws_json_1_1(
            value["recrawl_policy"]
        )
    if "lineage_configuration" in value:
        import aws_sdk_glue.types.lineage_configuration

        out["LineageConfiguration"] = (
            aws_sdk_glue.types.lineage_configuration.serialize_aws_json_1_1(
                value["lineage_configuration"]
            )
        )
    if "lake_formation_configuration" in value:
        import aws_sdk_glue.types.lake_formation_configuration

        out["LakeFormationConfiguration"] = (
            aws_sdk_glue.types.lake_formation_configuration.serialize_aws_json_1_1(
                value["lake_formation_configuration"]
            )
        )
    if "configuration" in value:
        out["Configuration"] = value["configuration"]
    if "crawler_security_configuration" in value:
        out["CrawlerSecurityConfiguration"] = value["crawler_security_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCrawlerRequest:
    out: UpdateCrawlerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateCrawlerRequest.name required")
    if "Role" in data:
        out["role"] = data["Role"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Targets" in data:
        import aws_sdk_glue.types.crawler_targets

        out["targets"] = aws_sdk_glue.types.crawler_targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    if "Classifiers" in data:
        import aws_sdk_glue.types.classifier_name_list

        out["classifiers"] = (
            aws_sdk_glue.types.classifier_name_list.deserialize_aws_json_1_1(
                data["Classifiers"]
            )
        )
    if "TablePrefix" in data:
        out["table_prefix"] = data["TablePrefix"]
    if "SchemaChangePolicy" in data:
        import aws_sdk_glue.types.schema_change_policy

        out["schema_change_policy"] = (
            aws_sdk_glue.types.schema_change_policy.deserialize_aws_json_1_1(
                data["SchemaChangePolicy"]
            )
        )
    if "RecrawlPolicy" in data:
        import aws_sdk_glue.types.recrawl_policy

        out["recrawl_policy"] = (
            aws_sdk_glue.types.recrawl_policy.deserialize_aws_json_1_1(
                data["RecrawlPolicy"]
            )
        )
    if "LineageConfiguration" in data:
        import aws_sdk_glue.types.lineage_configuration

        out["lineage_configuration"] = (
            aws_sdk_glue.types.lineage_configuration.deserialize_aws_json_1_1(
                data["LineageConfiguration"]
            )
        )
    if "LakeFormationConfiguration" in data:
        import aws_sdk_glue.types.lake_formation_configuration

        out["lake_formation_configuration"] = (
            aws_sdk_glue.types.lake_formation_configuration.deserialize_aws_json_1_1(
                data["LakeFormationConfiguration"]
            )
        )
    if "Configuration" in data:
        out["configuration"] = data["Configuration"]
    if "CrawlerSecurityConfiguration" in data:
        out["crawler_security_configuration"] = data["CrawlerSecurityConfiguration"]
    return out
