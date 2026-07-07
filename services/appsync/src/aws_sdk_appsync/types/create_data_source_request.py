"""Generated from Smithy shape ``com.amazonaws.appsync#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.data_source_level_metrics_config
    import aws_sdk_appsync.types.data_source_type
    import aws_sdk_appsync.types.dynamodb_data_source_config
    import aws_sdk_appsync.types.elasticsearch_data_source_config
    import aws_sdk_appsync.types.event_bridge_data_source_config
    import aws_sdk_appsync.types.http_data_source_config
    import aws_sdk_appsync.types.lambda_data_source_config
    import aws_sdk_appsync.types.open_search_service_data_source_config
    import aws_sdk_appsync.types.relational_database_data_source_config
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string


class CreateDataSourceRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID for the GraphQL API for the <code>DataSource</code>.</p>"""
    name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>A user-supplied name for the <code>DataSource</code>.</p>"""
    description: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>A description of the <code>DataSource</code>.</p>"""
    type: "aws_sdk_appsync.types.data_source_type.DataSourceType"
    """<p>The type of the <code>DataSource</code>.</p>"""
    service_role_arn: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The Identity and Access Management (IAM) service role Amazon Resource Name (ARN) for the data source. The system assumes this role when accessing the data source.</p>"""
    dynamodb_config: NotRequired[
        "aws_sdk_appsync.types.dynamodb_data_source_config.DynamodbDataSourceConfig"
    ]
    """<p>Amazon DynamoDB settings.</p>"""
    lambda_config: NotRequired[
        "aws_sdk_appsync.types.lambda_data_source_config.LambdaDataSourceConfig"
    ]
    """<p>Lambda settings.</p>"""
    elasticsearch_config: NotRequired[
        "aws_sdk_appsync.types.elasticsearch_data_source_config.ElasticsearchDataSourceConfig"
    ]
    """<p>Amazon OpenSearch Service settings.</p> <p>As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch Service. This configuration is deprecated. For new data sources, use <a>CreateDataSourceRequest$openSearchServiceConfig</a> to create an OpenSearch data source.</p>"""
    open_search_service_config: NotRequired[
        "aws_sdk_appsync.types.open_search_service_data_source_config.OpenSearchServiceDataSourceConfig"
    ]
    """<p>Amazon OpenSearch Service settings.</p>"""
    http_config: NotRequired[
        "aws_sdk_appsync.types.http_data_source_config.HttpDataSourceConfig"
    ]
    """<p>HTTP endpoint settings.</p>"""
    relational_database_config: NotRequired[
        "aws_sdk_appsync.types.relational_database_data_source_config.RelationalDatabaseDataSourceConfig"
    ]
    """<p>Relational database settings.</p>"""
    event_bridge_config: NotRequired[
        "aws_sdk_appsync.types.event_bridge_data_source_config.EventBridgeDataSourceConfig"
    ]
    """<p>Amazon EventBridge settings.</p>"""
    metrics_config: NotRequired[
        "aws_sdk_appsync.types.data_source_level_metrics_config.DataSourceLevelMetricsConfig"
    ]
    """<p>Enables or disables enhanced data source metrics for specified data sources. Note that <code>metricsConfig</code> won't be used unless the <code>dataSourceLevelMetricsBehavior</code> value is set to <code>PER_DATA_SOURCE_METRICS</code>. If the <code>dataSourceLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_DATA_SOURCE_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_appsync.types.data_source_type

    out["type"] = aws_sdk_appsync.types.data_source_type.serialize_json(value["type"])
    if "service_role_arn" in value:
        out["serviceRoleArn"] = value["service_role_arn"]
    if "dynamodb_config" in value:
        import aws_sdk_appsync.types.dynamodb_data_source_config

        out["dynamodbConfig"] = (
            aws_sdk_appsync.types.dynamodb_data_source_config.serialize_json(
                value["dynamodb_config"]
            )
        )
    if "lambda_config" in value:
        import aws_sdk_appsync.types.lambda_data_source_config

        out["lambdaConfig"] = (
            aws_sdk_appsync.types.lambda_data_source_config.serialize_json(
                value["lambda_config"]
            )
        )
    if "elasticsearch_config" in value:
        import aws_sdk_appsync.types.elasticsearch_data_source_config

        out["elasticsearchConfig"] = (
            aws_sdk_appsync.types.elasticsearch_data_source_config.serialize_json(
                value["elasticsearch_config"]
            )
        )
    if "open_search_service_config" in value:
        import aws_sdk_appsync.types.open_search_service_data_source_config

        out["openSearchServiceConfig"] = (
            aws_sdk_appsync.types.open_search_service_data_source_config.serialize_json(
                value["open_search_service_config"]
            )
        )
    if "http_config" in value:
        import aws_sdk_appsync.types.http_data_source_config

        out["httpConfig"] = (
            aws_sdk_appsync.types.http_data_source_config.serialize_json(
                value["http_config"]
            )
        )
    if "relational_database_config" in value:
        import aws_sdk_appsync.types.relational_database_data_source_config

        out["relationalDatabaseConfig"] = (
            aws_sdk_appsync.types.relational_database_data_source_config.serialize_json(
                value["relational_database_config"]
            )
        )
    if "event_bridge_config" in value:
        import aws_sdk_appsync.types.event_bridge_data_source_config

        out["eventBridgeConfig"] = (
            aws_sdk_appsync.types.event_bridge_data_source_config.serialize_json(
                value["event_bridge_config"]
            )
        )
    if "metrics_config" in value:
        import aws_sdk_appsync.types.data_source_level_metrics_config

        out["metricsConfig"] = (
            aws_sdk_appsync.types.data_source_level_metrics_config.serialize_json(
                value["metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataSourceRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_appsync.types.data_source_type

        out["type"] = aws_sdk_appsync.types.data_source_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateDataSourceRequest.type required")
    if "serviceRoleArn" in data:
        out["service_role_arn"] = data["serviceRoleArn"]
    if "dynamodbConfig" in data:
        import aws_sdk_appsync.types.dynamodb_data_source_config

        out["dynamodb_config"] = (
            aws_sdk_appsync.types.dynamodb_data_source_config.deserialize_json(
                data["dynamodbConfig"]
            )
        )
    if "lambdaConfig" in data:
        import aws_sdk_appsync.types.lambda_data_source_config

        out["lambda_config"] = (
            aws_sdk_appsync.types.lambda_data_source_config.deserialize_json(
                data["lambdaConfig"]
            )
        )
    if "elasticsearchConfig" in data:
        import aws_sdk_appsync.types.elasticsearch_data_source_config

        out["elasticsearch_config"] = (
            aws_sdk_appsync.types.elasticsearch_data_source_config.deserialize_json(
                data["elasticsearchConfig"]
            )
        )
    if "openSearchServiceConfig" in data:
        import aws_sdk_appsync.types.open_search_service_data_source_config

        out["open_search_service_config"] = (
            aws_sdk_appsync.types.open_search_service_data_source_config.deserialize_json(
                data["openSearchServiceConfig"]
            )
        )
    if "httpConfig" in data:
        import aws_sdk_appsync.types.http_data_source_config

        out["http_config"] = (
            aws_sdk_appsync.types.http_data_source_config.deserialize_json(
                data["httpConfig"]
            )
        )
    if "relationalDatabaseConfig" in data:
        import aws_sdk_appsync.types.relational_database_data_source_config

        out["relational_database_config"] = (
            aws_sdk_appsync.types.relational_database_data_source_config.deserialize_json(
                data["relationalDatabaseConfig"]
            )
        )
    if "eventBridgeConfig" in data:
        import aws_sdk_appsync.types.event_bridge_data_source_config

        out["event_bridge_config"] = (
            aws_sdk_appsync.types.event_bridge_data_source_config.deserialize_json(
                data["eventBridgeConfig"]
            )
        )
    if "metricsConfig" in data:
        import aws_sdk_appsync.types.data_source_level_metrics_config

        out["metrics_config"] = (
            aws_sdk_appsync.types.data_source_level_metrics_config.deserialize_json(
                data["metricsConfig"]
            )
        )
    return out
