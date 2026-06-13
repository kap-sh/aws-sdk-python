"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceParameters``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.amazon_elasticsearch_parameters
    import aws_sdk_quicksight.types.amazon_open_search_parameters
    import aws_sdk_quicksight.types.athena_parameters
    import aws_sdk_quicksight.types.aurora_parameters
    import aws_sdk_quicksight.types.aurora_postgre_sql_parameters
    import aws_sdk_quicksight.types.aws_iot_analytics_parameters
    import aws_sdk_quicksight.types.big_query_parameters
    import aws_sdk_quicksight.types.confluence_parameters
    import aws_sdk_quicksight.types.custom_connection_parameters
    import aws_sdk_quicksight.types.databricks_parameters
    import aws_sdk_quicksight.types.exasol_parameters
    import aws_sdk_quicksight.types.impala_parameters
    import aws_sdk_quicksight.types.jira_parameters
    import aws_sdk_quicksight.types.maria_db_parameters
    import aws_sdk_quicksight.types.my_sql_parameters
    import aws_sdk_quicksight.types.oracle_parameters
    import aws_sdk_quicksight.types.postgre_sql_parameters
    import aws_sdk_quicksight.types.presto_parameters
    import aws_sdk_quicksight.types.q_business_parameters
    import aws_sdk_quicksight.types.rds_parameters
    import aws_sdk_quicksight.types.redshift_parameters
    import aws_sdk_quicksight.types.s3_knowledge_base_parameters
    import aws_sdk_quicksight.types.s3_parameters
    import aws_sdk_quicksight.types.s3_tables_parameters
    import aws_sdk_quicksight.types.service_now_parameters
    import aws_sdk_quicksight.types.snowflake_parameters
    import aws_sdk_quicksight.types.spark_parameters
    import aws_sdk_quicksight.types.sql_server_parameters
    import aws_sdk_quicksight.types.starburst_parameters
    import aws_sdk_quicksight.types.teradata_parameters
    import aws_sdk_quicksight.types.trino_parameters
    import aws_sdk_quicksight.types.twitter_parameters
    import aws_sdk_quicksight.types.web_crawler_parameters


class _DataSourceParameters_AmazonElasticsearchParameters(TypedDict):
    AmazonElasticsearchParameters: "aws_sdk_quicksight.types.amazon_elasticsearch_parameters.AmazonElasticsearchParameters"


class _DataSourceParameters_AthenaParameters(TypedDict):
    AthenaParameters: "aws_sdk_quicksight.types.athena_parameters.AthenaParameters"


class _DataSourceParameters_AuroraParameters(TypedDict):
    AuroraParameters: "aws_sdk_quicksight.types.aurora_parameters.AuroraParameters"


class _DataSourceParameters_AuroraPostgreSqlParameters(TypedDict):
    AuroraPostgreSqlParameters: "aws_sdk_quicksight.types.aurora_postgre_sql_parameters.AuroraPostgreSqlParameters"


class _DataSourceParameters_AwsIotAnalyticsParameters(TypedDict):
    AwsIotAnalyticsParameters: "aws_sdk_quicksight.types.aws_iot_analytics_parameters.AwsIotAnalyticsParameters"


class _DataSourceParameters_JiraParameters(TypedDict):
    JiraParameters: "aws_sdk_quicksight.types.jira_parameters.JiraParameters"


class _DataSourceParameters_MariaDbParameters(TypedDict):
    MariaDbParameters: "aws_sdk_quicksight.types.maria_db_parameters.MariaDbParameters"


class _DataSourceParameters_MySqlParameters(TypedDict):
    MySqlParameters: "aws_sdk_quicksight.types.my_sql_parameters.MySqlParameters"


class _DataSourceParameters_OracleParameters(TypedDict):
    OracleParameters: "aws_sdk_quicksight.types.oracle_parameters.OracleParameters"


class _DataSourceParameters_PostgreSqlParameters(TypedDict):
    PostgreSqlParameters: (
        "aws_sdk_quicksight.types.postgre_sql_parameters.PostgreSqlParameters"
    )


class _DataSourceParameters_PrestoParameters(TypedDict):
    PrestoParameters: "aws_sdk_quicksight.types.presto_parameters.PrestoParameters"


class _DataSourceParameters_RdsParameters(TypedDict):
    RdsParameters: "aws_sdk_quicksight.types.rds_parameters.RdsParameters"


class _DataSourceParameters_RedshiftParameters(TypedDict):
    RedshiftParameters: (
        "aws_sdk_quicksight.types.redshift_parameters.RedshiftParameters"
    )


class _DataSourceParameters_S3Parameters(TypedDict):
    S3Parameters: "aws_sdk_quicksight.types.s3_parameters.S3Parameters"


class _DataSourceParameters_S3TablesParameters(TypedDict):
    S3TablesParameters: (
        "aws_sdk_quicksight.types.s3_tables_parameters.S3TablesParameters"
    )


class _DataSourceParameters_S3KnowledgeBaseParameters(TypedDict):
    S3KnowledgeBaseParameters: "aws_sdk_quicksight.types.s3_knowledge_base_parameters.S3KnowledgeBaseParameters"


class _DataSourceParameters_ServiceNowParameters(TypedDict):
    ServiceNowParameters: (
        "aws_sdk_quicksight.types.service_now_parameters.ServiceNowParameters"
    )


class _DataSourceParameters_SnowflakeParameters(TypedDict):
    SnowflakeParameters: (
        "aws_sdk_quicksight.types.snowflake_parameters.SnowflakeParameters"
    )


class _DataSourceParameters_SparkParameters(TypedDict):
    SparkParameters: "aws_sdk_quicksight.types.spark_parameters.SparkParameters"


class _DataSourceParameters_SqlServerParameters(TypedDict):
    SqlServerParameters: (
        "aws_sdk_quicksight.types.sql_server_parameters.SqlServerParameters"
    )


class _DataSourceParameters_TeradataParameters(TypedDict):
    TeradataParameters: (
        "aws_sdk_quicksight.types.teradata_parameters.TeradataParameters"
    )


class _DataSourceParameters_TwitterParameters(TypedDict):
    TwitterParameters: "aws_sdk_quicksight.types.twitter_parameters.TwitterParameters"


class _DataSourceParameters_AmazonOpenSearchParameters(TypedDict):
    AmazonOpenSearchParameters: "aws_sdk_quicksight.types.amazon_open_search_parameters.AmazonOpenSearchParameters"


class _DataSourceParameters_ExasolParameters(TypedDict):
    ExasolParameters: "aws_sdk_quicksight.types.exasol_parameters.ExasolParameters"


class _DataSourceParameters_DatabricksParameters(TypedDict):
    DatabricksParameters: (
        "aws_sdk_quicksight.types.databricks_parameters.DatabricksParameters"
    )


class _DataSourceParameters_StarburstParameters(TypedDict):
    StarburstParameters: (
        "aws_sdk_quicksight.types.starburst_parameters.StarburstParameters"
    )


class _DataSourceParameters_TrinoParameters(TypedDict):
    TrinoParameters: "aws_sdk_quicksight.types.trino_parameters.TrinoParameters"


class _DataSourceParameters_BigQueryParameters(TypedDict):
    BigQueryParameters: (
        "aws_sdk_quicksight.types.big_query_parameters.BigQueryParameters"
    )


class _DataSourceParameters_ImpalaParameters(TypedDict):
    ImpalaParameters: "aws_sdk_quicksight.types.impala_parameters.ImpalaParameters"


class _DataSourceParameters_CustomConnectionParameters(TypedDict):
    CustomConnectionParameters: "aws_sdk_quicksight.types.custom_connection_parameters.CustomConnectionParameters"


class _DataSourceParameters_WebCrawlerParameters(TypedDict):
    WebCrawlerParameters: (
        "aws_sdk_quicksight.types.web_crawler_parameters.WebCrawlerParameters"
    )


class _DataSourceParameters_ConfluenceParameters(TypedDict):
    ConfluenceParameters: (
        "aws_sdk_quicksight.types.confluence_parameters.ConfluenceParameters"
    )


class _DataSourceParameters_QBusinessParameters(TypedDict):
    QBusinessParameters: (
        "aws_sdk_quicksight.types.q_business_parameters.QBusinessParameters"
    )


DataSourceParameters: TypeAlias = (
    _DataSourceParameters_AmazonElasticsearchParameters
    | _DataSourceParameters_AthenaParameters
    | _DataSourceParameters_AuroraParameters
    | _DataSourceParameters_AuroraPostgreSqlParameters
    | _DataSourceParameters_AwsIotAnalyticsParameters
    | _DataSourceParameters_JiraParameters
    | _DataSourceParameters_MariaDbParameters
    | _DataSourceParameters_MySqlParameters
    | _DataSourceParameters_OracleParameters
    | _DataSourceParameters_PostgreSqlParameters
    | _DataSourceParameters_PrestoParameters
    | _DataSourceParameters_RdsParameters
    | _DataSourceParameters_RedshiftParameters
    | _DataSourceParameters_S3Parameters
    | _DataSourceParameters_S3TablesParameters
    | _DataSourceParameters_S3KnowledgeBaseParameters
    | _DataSourceParameters_ServiceNowParameters
    | _DataSourceParameters_SnowflakeParameters
    | _DataSourceParameters_SparkParameters
    | _DataSourceParameters_SqlServerParameters
    | _DataSourceParameters_TeradataParameters
    | _DataSourceParameters_TwitterParameters
    | _DataSourceParameters_AmazonOpenSearchParameters
    | _DataSourceParameters_ExasolParameters
    | _DataSourceParameters_DatabricksParameters
    | _DataSourceParameters_StarburstParameters
    | _DataSourceParameters_TrinoParameters
    | _DataSourceParameters_BigQueryParameters
    | _DataSourceParameters_ImpalaParameters
    | _DataSourceParameters_CustomConnectionParameters
    | _DataSourceParameters_WebCrawlerParameters
    | _DataSourceParameters_ConfluenceParameters
    | _DataSourceParameters_QBusinessParameters
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceParameters) -> dict:
    if "AmazonElasticsearchParameters" in value:
        import aws_sdk_quicksight.types.amazon_elasticsearch_parameters

        return {
            "AmazonElasticsearchParameters": aws_sdk_quicksight.types.amazon_elasticsearch_parameters.serialize_json(
                value["AmazonElasticsearchParameters"]
            )
        }
    elif "AthenaParameters" in value:
        import aws_sdk_quicksight.types.athena_parameters

        return {
            "AthenaParameters": aws_sdk_quicksight.types.athena_parameters.serialize_json(
                value["AthenaParameters"]
            )
        }
    elif "AuroraParameters" in value:
        import aws_sdk_quicksight.types.aurora_parameters

        return {
            "AuroraParameters": aws_sdk_quicksight.types.aurora_parameters.serialize_json(
                value["AuroraParameters"]
            )
        }
    elif "AuroraPostgreSqlParameters" in value:
        import aws_sdk_quicksight.types.aurora_postgre_sql_parameters

        return {
            "AuroraPostgreSqlParameters": aws_sdk_quicksight.types.aurora_postgre_sql_parameters.serialize_json(
                value["AuroraPostgreSqlParameters"]
            )
        }
    elif "AwsIotAnalyticsParameters" in value:
        import aws_sdk_quicksight.types.aws_iot_analytics_parameters

        return {
            "AwsIotAnalyticsParameters": aws_sdk_quicksight.types.aws_iot_analytics_parameters.serialize_json(
                value["AwsIotAnalyticsParameters"]
            )
        }
    elif "JiraParameters" in value:
        import aws_sdk_quicksight.types.jira_parameters

        return {
            "JiraParameters": aws_sdk_quicksight.types.jira_parameters.serialize_json(
                value["JiraParameters"]
            )
        }
    elif "MariaDbParameters" in value:
        import aws_sdk_quicksight.types.maria_db_parameters

        return {
            "MariaDbParameters": aws_sdk_quicksight.types.maria_db_parameters.serialize_json(
                value["MariaDbParameters"]
            )
        }
    elif "MySqlParameters" in value:
        import aws_sdk_quicksight.types.my_sql_parameters

        return {
            "MySqlParameters": aws_sdk_quicksight.types.my_sql_parameters.serialize_json(
                value["MySqlParameters"]
            )
        }
    elif "OracleParameters" in value:
        import aws_sdk_quicksight.types.oracle_parameters

        return {
            "OracleParameters": aws_sdk_quicksight.types.oracle_parameters.serialize_json(
                value["OracleParameters"]
            )
        }
    elif "PostgreSqlParameters" in value:
        import aws_sdk_quicksight.types.postgre_sql_parameters

        return {
            "PostgreSqlParameters": aws_sdk_quicksight.types.postgre_sql_parameters.serialize_json(
                value["PostgreSqlParameters"]
            )
        }
    elif "PrestoParameters" in value:
        import aws_sdk_quicksight.types.presto_parameters

        return {
            "PrestoParameters": aws_sdk_quicksight.types.presto_parameters.serialize_json(
                value["PrestoParameters"]
            )
        }
    elif "RdsParameters" in value:
        import aws_sdk_quicksight.types.rds_parameters

        return {
            "RdsParameters": aws_sdk_quicksight.types.rds_parameters.serialize_json(
                value["RdsParameters"]
            )
        }
    elif "RedshiftParameters" in value:
        import aws_sdk_quicksight.types.redshift_parameters

        return {
            "RedshiftParameters": aws_sdk_quicksight.types.redshift_parameters.serialize_json(
                value["RedshiftParameters"]
            )
        }
    elif "S3Parameters" in value:
        import aws_sdk_quicksight.types.s3_parameters

        return {
            "S3Parameters": aws_sdk_quicksight.types.s3_parameters.serialize_json(
                value["S3Parameters"]
            )
        }
    elif "S3TablesParameters" in value:
        import aws_sdk_quicksight.types.s3_tables_parameters

        return {
            "S3TablesParameters": aws_sdk_quicksight.types.s3_tables_parameters.serialize_json(
                value["S3TablesParameters"]
            )
        }
    elif "S3KnowledgeBaseParameters" in value:
        import aws_sdk_quicksight.types.s3_knowledge_base_parameters

        return {
            "S3KnowledgeBaseParameters": aws_sdk_quicksight.types.s3_knowledge_base_parameters.serialize_json(
                value["S3KnowledgeBaseParameters"]
            )
        }
    elif "ServiceNowParameters" in value:
        import aws_sdk_quicksight.types.service_now_parameters

        return {
            "ServiceNowParameters": aws_sdk_quicksight.types.service_now_parameters.serialize_json(
                value["ServiceNowParameters"]
            )
        }
    elif "SnowflakeParameters" in value:
        import aws_sdk_quicksight.types.snowflake_parameters

        return {
            "SnowflakeParameters": aws_sdk_quicksight.types.snowflake_parameters.serialize_json(
                value["SnowflakeParameters"]
            )
        }
    elif "SparkParameters" in value:
        import aws_sdk_quicksight.types.spark_parameters

        return {
            "SparkParameters": aws_sdk_quicksight.types.spark_parameters.serialize_json(
                value["SparkParameters"]
            )
        }
    elif "SqlServerParameters" in value:
        import aws_sdk_quicksight.types.sql_server_parameters

        return {
            "SqlServerParameters": aws_sdk_quicksight.types.sql_server_parameters.serialize_json(
                value["SqlServerParameters"]
            )
        }
    elif "TeradataParameters" in value:
        import aws_sdk_quicksight.types.teradata_parameters

        return {
            "TeradataParameters": aws_sdk_quicksight.types.teradata_parameters.serialize_json(
                value["TeradataParameters"]
            )
        }
    elif "TwitterParameters" in value:
        import aws_sdk_quicksight.types.twitter_parameters

        return {
            "TwitterParameters": aws_sdk_quicksight.types.twitter_parameters.serialize_json(
                value["TwitterParameters"]
            )
        }
    elif "AmazonOpenSearchParameters" in value:
        import aws_sdk_quicksight.types.amazon_open_search_parameters

        return {
            "AmazonOpenSearchParameters": aws_sdk_quicksight.types.amazon_open_search_parameters.serialize_json(
                value["AmazonOpenSearchParameters"]
            )
        }
    elif "ExasolParameters" in value:
        import aws_sdk_quicksight.types.exasol_parameters

        return {
            "ExasolParameters": aws_sdk_quicksight.types.exasol_parameters.serialize_json(
                value["ExasolParameters"]
            )
        }
    elif "DatabricksParameters" in value:
        import aws_sdk_quicksight.types.databricks_parameters

        return {
            "DatabricksParameters": aws_sdk_quicksight.types.databricks_parameters.serialize_json(
                value["DatabricksParameters"]
            )
        }
    elif "StarburstParameters" in value:
        import aws_sdk_quicksight.types.starburst_parameters

        return {
            "StarburstParameters": aws_sdk_quicksight.types.starburst_parameters.serialize_json(
                value["StarburstParameters"]
            )
        }
    elif "TrinoParameters" in value:
        import aws_sdk_quicksight.types.trino_parameters

        return {
            "TrinoParameters": aws_sdk_quicksight.types.trino_parameters.serialize_json(
                value["TrinoParameters"]
            )
        }
    elif "BigQueryParameters" in value:
        import aws_sdk_quicksight.types.big_query_parameters

        return {
            "BigQueryParameters": aws_sdk_quicksight.types.big_query_parameters.serialize_json(
                value["BigQueryParameters"]
            )
        }
    elif "ImpalaParameters" in value:
        import aws_sdk_quicksight.types.impala_parameters

        return {
            "ImpalaParameters": aws_sdk_quicksight.types.impala_parameters.serialize_json(
                value["ImpalaParameters"]
            )
        }
    elif "CustomConnectionParameters" in value:
        import aws_sdk_quicksight.types.custom_connection_parameters

        return {
            "CustomConnectionParameters": aws_sdk_quicksight.types.custom_connection_parameters.serialize_json(
                value["CustomConnectionParameters"]
            )
        }
    elif "WebCrawlerParameters" in value:
        import aws_sdk_quicksight.types.web_crawler_parameters

        return {
            "WebCrawlerParameters": aws_sdk_quicksight.types.web_crawler_parameters.serialize_json(
                value["WebCrawlerParameters"]
            )
        }
    elif "ConfluenceParameters" in value:
        import aws_sdk_quicksight.types.confluence_parameters

        return {
            "ConfluenceParameters": aws_sdk_quicksight.types.confluence_parameters.serialize_json(
                value["ConfluenceParameters"]
            )
        }
    elif "QBusinessParameters" in value:
        import aws_sdk_quicksight.types.q_business_parameters

        return {
            "QBusinessParameters": aws_sdk_quicksight.types.q_business_parameters.serialize_json(
                value["QBusinessParameters"]
            )
        }
    else:
        raise SerializationError("DataSourceParameters: no variant present")


def deserialize_json(data: dict) -> DataSourceParameters:
    if "AmazonElasticsearchParameters" in data:
        import aws_sdk_quicksight.types.amazon_elasticsearch_parameters

        return {
            "AmazonElasticsearchParameters": aws_sdk_quicksight.types.amazon_elasticsearch_parameters.deserialize_json(
                data["AmazonElasticsearchParameters"]
            )
        }
    elif "AthenaParameters" in data:
        import aws_sdk_quicksight.types.athena_parameters

        return {
            "AthenaParameters": aws_sdk_quicksight.types.athena_parameters.deserialize_json(
                data["AthenaParameters"]
            )
        }
    elif "AuroraParameters" in data:
        import aws_sdk_quicksight.types.aurora_parameters

        return {
            "AuroraParameters": aws_sdk_quicksight.types.aurora_parameters.deserialize_json(
                data["AuroraParameters"]
            )
        }
    elif "AuroraPostgreSqlParameters" in data:
        import aws_sdk_quicksight.types.aurora_postgre_sql_parameters

        return {
            "AuroraPostgreSqlParameters": aws_sdk_quicksight.types.aurora_postgre_sql_parameters.deserialize_json(
                data["AuroraPostgreSqlParameters"]
            )
        }
    elif "AwsIotAnalyticsParameters" in data:
        import aws_sdk_quicksight.types.aws_iot_analytics_parameters

        return {
            "AwsIotAnalyticsParameters": aws_sdk_quicksight.types.aws_iot_analytics_parameters.deserialize_json(
                data["AwsIotAnalyticsParameters"]
            )
        }
    elif "JiraParameters" in data:
        import aws_sdk_quicksight.types.jira_parameters

        return {
            "JiraParameters": aws_sdk_quicksight.types.jira_parameters.deserialize_json(
                data["JiraParameters"]
            )
        }
    elif "MariaDbParameters" in data:
        import aws_sdk_quicksight.types.maria_db_parameters

        return {
            "MariaDbParameters": aws_sdk_quicksight.types.maria_db_parameters.deserialize_json(
                data["MariaDbParameters"]
            )
        }
    elif "MySqlParameters" in data:
        import aws_sdk_quicksight.types.my_sql_parameters

        return {
            "MySqlParameters": aws_sdk_quicksight.types.my_sql_parameters.deserialize_json(
                data["MySqlParameters"]
            )
        }
    elif "OracleParameters" in data:
        import aws_sdk_quicksight.types.oracle_parameters

        return {
            "OracleParameters": aws_sdk_quicksight.types.oracle_parameters.deserialize_json(
                data["OracleParameters"]
            )
        }
    elif "PostgreSqlParameters" in data:
        import aws_sdk_quicksight.types.postgre_sql_parameters

        return {
            "PostgreSqlParameters": aws_sdk_quicksight.types.postgre_sql_parameters.deserialize_json(
                data["PostgreSqlParameters"]
            )
        }
    elif "PrestoParameters" in data:
        import aws_sdk_quicksight.types.presto_parameters

        return {
            "PrestoParameters": aws_sdk_quicksight.types.presto_parameters.deserialize_json(
                data["PrestoParameters"]
            )
        }
    elif "RdsParameters" in data:
        import aws_sdk_quicksight.types.rds_parameters

        return {
            "RdsParameters": aws_sdk_quicksight.types.rds_parameters.deserialize_json(
                data["RdsParameters"]
            )
        }
    elif "RedshiftParameters" in data:
        import aws_sdk_quicksight.types.redshift_parameters

        return {
            "RedshiftParameters": aws_sdk_quicksight.types.redshift_parameters.deserialize_json(
                data["RedshiftParameters"]
            )
        }
    elif "S3Parameters" in data:
        import aws_sdk_quicksight.types.s3_parameters

        return {
            "S3Parameters": aws_sdk_quicksight.types.s3_parameters.deserialize_json(
                data["S3Parameters"]
            )
        }
    elif "S3TablesParameters" in data:
        import aws_sdk_quicksight.types.s3_tables_parameters

        return {
            "S3TablesParameters": aws_sdk_quicksight.types.s3_tables_parameters.deserialize_json(
                data["S3TablesParameters"]
            )
        }
    elif "S3KnowledgeBaseParameters" in data:
        import aws_sdk_quicksight.types.s3_knowledge_base_parameters

        return {
            "S3KnowledgeBaseParameters": aws_sdk_quicksight.types.s3_knowledge_base_parameters.deserialize_json(
                data["S3KnowledgeBaseParameters"]
            )
        }
    elif "ServiceNowParameters" in data:
        import aws_sdk_quicksight.types.service_now_parameters

        return {
            "ServiceNowParameters": aws_sdk_quicksight.types.service_now_parameters.deserialize_json(
                data["ServiceNowParameters"]
            )
        }
    elif "SnowflakeParameters" in data:
        import aws_sdk_quicksight.types.snowflake_parameters

        return {
            "SnowflakeParameters": aws_sdk_quicksight.types.snowflake_parameters.deserialize_json(
                data["SnowflakeParameters"]
            )
        }
    elif "SparkParameters" in data:
        import aws_sdk_quicksight.types.spark_parameters

        return {
            "SparkParameters": aws_sdk_quicksight.types.spark_parameters.deserialize_json(
                data["SparkParameters"]
            )
        }
    elif "SqlServerParameters" in data:
        import aws_sdk_quicksight.types.sql_server_parameters

        return {
            "SqlServerParameters": aws_sdk_quicksight.types.sql_server_parameters.deserialize_json(
                data["SqlServerParameters"]
            )
        }
    elif "TeradataParameters" in data:
        import aws_sdk_quicksight.types.teradata_parameters

        return {
            "TeradataParameters": aws_sdk_quicksight.types.teradata_parameters.deserialize_json(
                data["TeradataParameters"]
            )
        }
    elif "TwitterParameters" in data:
        import aws_sdk_quicksight.types.twitter_parameters

        return {
            "TwitterParameters": aws_sdk_quicksight.types.twitter_parameters.deserialize_json(
                data["TwitterParameters"]
            )
        }
    elif "AmazonOpenSearchParameters" in data:
        import aws_sdk_quicksight.types.amazon_open_search_parameters

        return {
            "AmazonOpenSearchParameters": aws_sdk_quicksight.types.amazon_open_search_parameters.deserialize_json(
                data["AmazonOpenSearchParameters"]
            )
        }
    elif "ExasolParameters" in data:
        import aws_sdk_quicksight.types.exasol_parameters

        return {
            "ExasolParameters": aws_sdk_quicksight.types.exasol_parameters.deserialize_json(
                data["ExasolParameters"]
            )
        }
    elif "DatabricksParameters" in data:
        import aws_sdk_quicksight.types.databricks_parameters

        return {
            "DatabricksParameters": aws_sdk_quicksight.types.databricks_parameters.deserialize_json(
                data["DatabricksParameters"]
            )
        }
    elif "StarburstParameters" in data:
        import aws_sdk_quicksight.types.starburst_parameters

        return {
            "StarburstParameters": aws_sdk_quicksight.types.starburst_parameters.deserialize_json(
                data["StarburstParameters"]
            )
        }
    elif "TrinoParameters" in data:
        import aws_sdk_quicksight.types.trino_parameters

        return {
            "TrinoParameters": aws_sdk_quicksight.types.trino_parameters.deserialize_json(
                data["TrinoParameters"]
            )
        }
    elif "BigQueryParameters" in data:
        import aws_sdk_quicksight.types.big_query_parameters

        return {
            "BigQueryParameters": aws_sdk_quicksight.types.big_query_parameters.deserialize_json(
                data["BigQueryParameters"]
            )
        }
    elif "ImpalaParameters" in data:
        import aws_sdk_quicksight.types.impala_parameters

        return {
            "ImpalaParameters": aws_sdk_quicksight.types.impala_parameters.deserialize_json(
                data["ImpalaParameters"]
            )
        }
    elif "CustomConnectionParameters" in data:
        import aws_sdk_quicksight.types.custom_connection_parameters

        return {
            "CustomConnectionParameters": aws_sdk_quicksight.types.custom_connection_parameters.deserialize_json(
                data["CustomConnectionParameters"]
            )
        }
    elif "WebCrawlerParameters" in data:
        import aws_sdk_quicksight.types.web_crawler_parameters

        return {
            "WebCrawlerParameters": aws_sdk_quicksight.types.web_crawler_parameters.deserialize_json(
                data["WebCrawlerParameters"]
            )
        }
    elif "ConfluenceParameters" in data:
        import aws_sdk_quicksight.types.confluence_parameters

        return {
            "ConfluenceParameters": aws_sdk_quicksight.types.confluence_parameters.deserialize_json(
                data["ConfluenceParameters"]
            )
        }
    elif "QBusinessParameters" in data:
        import aws_sdk_quicksight.types.q_business_parameters

        return {
            "QBusinessParameters": aws_sdk_quicksight.types.q_business_parameters.deserialize_json(
                data["QBusinessParameters"]
            )
        }
    else:
        raise DeserializationError("DataSourceParameters: no recognized variant key")
