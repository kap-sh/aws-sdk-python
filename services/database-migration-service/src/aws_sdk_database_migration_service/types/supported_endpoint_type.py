"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SupportedEndpointType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean
    import aws_sdk_database_migration_service.types.replication_endpoint_type_value
    import aws_sdk_database_migration_service.types.string


class SupportedEndpointType(TypedDict):
    engine_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p>The database engine name. Valid values, depending on the EndpointType, include <code>\"mysql\"</code>, <code>\"oracle\"</code>, <code>\"postgres\"</code>, <code>\"mariadb\"</code>, <code>\"aurora\"</code>, <code>\"aurora-postgresql\"</code>, <code>\"redshift\"</code>, <code>\"s3\"</code>, <code>\"db2\"</code>, <code>\"db2-zos\"</code>, <code>\"azuredb\"</code>, <code>\"sybase\"</code>, <code>\"dynamodb\"</code>, <code>\"mongodb\"</code>, <code>\"kinesis\"</code>, <code>\"kafka\"</code>, <code>\"elasticsearch\"</code>, <code>\"documentdb\"</code>, <code>\"sqlserver\"</code>, <code>\"neptune\"</code>, and <code>\"babelfish\"</code>.</p>"""
    supports_cdc: "aws_sdk_database_migration_service.types.boolean.Boolean"
    """<p>Indicates if change data capture (CDC) is supported.</p>"""
    endpoint_type: NotRequired[
        "aws_sdk_database_migration_service.types.replication_endpoint_type_value.ReplicationEndpointTypeValue"
    ]
    """<p>The type of endpoint. Valid values are <code>source</code> and <code>target</code>.</p>"""
    replication_instance_engine_minimum_version: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The earliest DMS engine version that supports this endpoint engine. Note that endpoint engines released with DMS versions earlier than 3.1.1 do not return a value for this parameter.</p>"""
    engine_display_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    r"""<p>The expanded name for the engine name. For example, if the <code>EngineName</code> parameter is \"aurora\", this value would be \"Amazon Aurora MySQL\".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedEndpointType) -> dict:
    out: dict = {}
    if "engine_name" in value:
        out["EngineName"] = value["engine_name"]
    out["SupportsCDC"] = value.get("supports_cdc", False)
    if "endpoint_type" in value:
        import aws_sdk_database_migration_service.types.replication_endpoint_type_value

        out["EndpointType"] = (
            aws_sdk_database_migration_service.types.replication_endpoint_type_value.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    if "replication_instance_engine_minimum_version" in value:
        out["ReplicationInstanceEngineMinimumVersion"] = value[
            "replication_instance_engine_minimum_version"
        ]
    if "engine_display_name" in value:
        out["EngineDisplayName"] = value["engine_display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedEndpointType:
    out: SupportedEndpointType = {}  # type: ignore[typeddict-item]
    if "EngineName" in data:
        out["engine_name"] = data["EngineName"]
    if "SupportsCDC" in data:
        out["supports_cdc"] = data["SupportsCDC"]
    else:
        out["supports_cdc"] = False
    if "EndpointType" in data:
        import aws_sdk_database_migration_service.types.replication_endpoint_type_value

        out["endpoint_type"] = (
            aws_sdk_database_migration_service.types.replication_endpoint_type_value.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if "ReplicationInstanceEngineMinimumVersion" in data:
        out["replication_instance_engine_minimum_version"] = data[
            "ReplicationInstanceEngineMinimumVersion"
        ]
    if "EngineDisplayName" in data:
        out["engine_display_name"] = data["EngineDisplayName"]
    return out
