"""Generated from Smithy shape ``com.amazonaws.glue#Crawler``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.classifier_name_list
    import aws_sdk_glue.types.crawler_configuration
    import aws_sdk_glue.types.crawler_security_configuration
    import aws_sdk_glue.types.crawler_state
    import aws_sdk_glue.types.crawler_targets
    import aws_sdk_glue.types.database_name
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.lake_formation_configuration
    import aws_sdk_glue.types.last_crawl_info
    import aws_sdk_glue.types.lineage_configuration
    import aws_sdk_glue.types.milliseconds_count
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.recrawl_policy
    import aws_sdk_glue.types.role
    import aws_sdk_glue.types.schedule
    import aws_sdk_glue.types.schema_change_policy
    import aws_sdk_glue.types.table_prefix
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.version_id


class Crawler(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the crawler.</p>"""
    role: NotRequired["aws_sdk_glue.types.role.Role"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.</p>"""
    targets: NotRequired["aws_sdk_glue.types.crawler_targets.CrawlerTargets"]
    """<p>A collection of targets to crawl.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.database_name.DatabaseName"]
    """<p>The name of the database in which the crawler's output is stored.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the crawler.</p>"""
    classifiers: NotRequired[
        "aws_sdk_glue.types.classifier_name_list.ClassifierNameList"
    ]
    """<p>A list of UTF-8 strings that specify the custom classifiers that are associated with the crawler.</p>"""
    recrawl_policy: NotRequired["aws_sdk_glue.types.recrawl_policy.RecrawlPolicy"]
    """<p>A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.schema_change_policy.SchemaChangePolicy"
    ]
    """<p>The policy that specifies update and delete behaviors for the crawler.</p>"""
    lineage_configuration: NotRequired[
        "aws_sdk_glue.types.lineage_configuration.LineageConfiguration"
    ]
    """<p>A configuration that specifies whether data lineage is enabled for the crawler.</p>"""
    state: NotRequired["aws_sdk_glue.types.crawler_state.CrawlerState"]
    """<p>Indicates whether the crawler is running, or whether a run is pending.</p>"""
    table_prefix: NotRequired["aws_sdk_glue.types.table_prefix.TablePrefix"]
    """<p>The prefix added to the names of tables that are created.</p>"""
    schedule: NotRequired["aws_sdk_glue.types.schedule.Schedule"]
    """<p>For scheduled crawlers, the schedule when the crawler runs.</p>"""
    crawl_elapsed_time: "aws_sdk_glue.types.milliseconds_count.MillisecondsCount"
    """<p>If the crawler is running, contains the total time elapsed since the last crawl began.</p>"""
    creation_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that the crawler was created.</p>"""
    last_updated: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that the crawler was last updated.</p>"""
    last_crawl: NotRequired["aws_sdk_glue.types.last_crawl_info.LastCrawlInfo"]
    """<p>The status of the last crawl, and potentially error information if an error occurred.</p>"""
    version: "aws_sdk_glue.types.version_id.VersionId"
    """<p>The version of the crawler.</p>"""
    configuration: NotRequired[
        "aws_sdk_glue.types.crawler_configuration.CrawlerConfiguration"
    ]
    r"""<p>Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html\">Setting crawler configuration options</a>.</p>"""
    crawler_security_configuration: NotRequired[
        "aws_sdk_glue.types.crawler_security_configuration.CrawlerSecurityConfiguration"
    ]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used by this crawler.</p>"""
    lake_formation_configuration: NotRequired[
        "aws_sdk_glue.types.lake_formation_configuration.LakeFormationConfiguration"
    ]
    """<p>Specifies whether the crawler should use Lake Formation credentials for the crawler instead of the IAM role credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Crawler) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "role" in value:
        out["Role"] = value["role"]
    if "targets" in value:
        import aws_sdk_glue.types.crawler_targets

        out["Targets"] = aws_sdk_glue.types.crawler_targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "classifiers" in value:
        import aws_sdk_glue.types.classifier_name_list

        out["Classifiers"] = (
            aws_sdk_glue.types.classifier_name_list.serialize_aws_json_1_1(
                value["classifiers"]
            )
        )
    if "recrawl_policy" in value:
        import aws_sdk_glue.types.recrawl_policy

        out["RecrawlPolicy"] = aws_sdk_glue.types.recrawl_policy.serialize_aws_json_1_1(
            value["recrawl_policy"]
        )
    if "schema_change_policy" in value:
        import aws_sdk_glue.types.schema_change_policy

        out["SchemaChangePolicy"] = (
            aws_sdk_glue.types.schema_change_policy.serialize_aws_json_1_1(
                value["schema_change_policy"]
            )
        )
    if "lineage_configuration" in value:
        import aws_sdk_glue.types.lineage_configuration

        out["LineageConfiguration"] = (
            aws_sdk_glue.types.lineage_configuration.serialize_aws_json_1_1(
                value["lineage_configuration"]
            )
        )
    if "state" in value:
        import aws_sdk_glue.types.crawler_state

        out["State"] = aws_sdk_glue.types.crawler_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "table_prefix" in value:
        out["TablePrefix"] = value["table_prefix"]
    if "schedule" in value:
        import aws_sdk_glue.types.schedule

        out["Schedule"] = aws_sdk_glue.types.schedule.serialize_aws_json_1_1(
            value["schedule"]
        )
    out["CrawlElapsedTime"] = value.get("crawl_elapsed_time", 0)
    if "creation_time" in value:
        import aws_sdk_glue.types.timestamp

        out["CreationTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import aws_sdk_glue.types.timestamp

        out["LastUpdated"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    if "last_crawl" in value:
        import aws_sdk_glue.types.last_crawl_info

        out["LastCrawl"] = aws_sdk_glue.types.last_crawl_info.serialize_aws_json_1_1(
            value["last_crawl"]
        )
    out["Version"] = value.get("version", 0)
    if "configuration" in value:
        out["Configuration"] = value["configuration"]
    if "crawler_security_configuration" in value:
        out["CrawlerSecurityConfiguration"] = value["crawler_security_configuration"]
    if "lake_formation_configuration" in value:
        import aws_sdk_glue.types.lake_formation_configuration

        out["LakeFormationConfiguration"] = (
            aws_sdk_glue.types.lake_formation_configuration.serialize_aws_json_1_1(
                value["lake_formation_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Crawler:
    out: Crawler = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "Targets" in data:
        import aws_sdk_glue.types.crawler_targets

        out["targets"] = aws_sdk_glue.types.crawler_targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Classifiers" in data:
        import aws_sdk_glue.types.classifier_name_list

        out["classifiers"] = (
            aws_sdk_glue.types.classifier_name_list.deserialize_aws_json_1_1(
                data["Classifiers"]
            )
        )
    if "RecrawlPolicy" in data:
        import aws_sdk_glue.types.recrawl_policy

        out["recrawl_policy"] = (
            aws_sdk_glue.types.recrawl_policy.deserialize_aws_json_1_1(
                data["RecrawlPolicy"]
            )
        )
    if "SchemaChangePolicy" in data:
        import aws_sdk_glue.types.schema_change_policy

        out["schema_change_policy"] = (
            aws_sdk_glue.types.schema_change_policy.deserialize_aws_json_1_1(
                data["SchemaChangePolicy"]
            )
        )
    if "LineageConfiguration" in data:
        import aws_sdk_glue.types.lineage_configuration

        out["lineage_configuration"] = (
            aws_sdk_glue.types.lineage_configuration.deserialize_aws_json_1_1(
                data["LineageConfiguration"]
            )
        )
    if "State" in data:
        import aws_sdk_glue.types.crawler_state

        out["state"] = aws_sdk_glue.types.crawler_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "TablePrefix" in data:
        out["table_prefix"] = data["TablePrefix"]
    if "Schedule" in data:
        import aws_sdk_glue.types.schedule

        out["schedule"] = aws_sdk_glue.types.schedule.deserialize_aws_json_1_1(
            data["Schedule"]
        )
    if "CrawlElapsedTime" in data:
        out["crawl_elapsed_time"] = data["CrawlElapsedTime"]
    else:
        out["crawl_elapsed_time"] = 0
    if "CreationTime" in data:
        import aws_sdk_glue.types.timestamp

        out["creation_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastUpdated" in data:
        import aws_sdk_glue.types.timestamp

        out["last_updated"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if "LastCrawl" in data:
        import aws_sdk_glue.types.last_crawl_info

        out["last_crawl"] = aws_sdk_glue.types.last_crawl_info.deserialize_aws_json_1_1(
            data["LastCrawl"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "Configuration" in data:
        out["configuration"] = data["Configuration"]
    if "CrawlerSecurityConfiguration" in data:
        out["crawler_security_configuration"] = data["CrawlerSecurityConfiguration"]
    if "LakeFormationConfiguration" in data:
        import aws_sdk_glue.types.lake_formation_configuration

        out["lake_formation_configuration"] = (
            aws_sdk_glue.types.lake_formation_configuration.deserialize_aws_json_1_1(
                data["LakeFormationConfiguration"]
            )
        )
    return out
