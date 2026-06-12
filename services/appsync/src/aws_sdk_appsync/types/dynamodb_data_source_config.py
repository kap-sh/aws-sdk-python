"""Generated from Smithy shape ``com.amazonaws.appsync#DynamodbDataSourceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.boolean
    import aws_sdk_appsync.types.delta_sync_config
    import aws_sdk_appsync.types.string


class DynamodbDataSourceConfig(TypedDict):
    table_name: "aws_sdk_appsync.types.string.String"
    """<p>The table name.</p>"""
    aws_region: "aws_sdk_appsync.types.string.String"
    """<p>The Amazon Web Services Region.</p>"""
    use_caller_credentials: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>Set to TRUE to use Amazon Cognito credentials with this data source.</p>"""
    delta_sync_config: NotRequired[
        "aws_sdk_appsync.types.delta_sync_config.DeltaSyncConfig"
    ]
    """<p>The <code>DeltaSyncConfig</code> for a versioned data source.</p>"""
    versioned: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>Set to TRUE to use Conflict Detection and Resolution with this data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamodbDataSourceConfig) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    out["awsRegion"] = value["aws_region"]
    out["useCallerCredentials"] = value.get("use_caller_credentials", False)
    if "delta_sync_config" in value:
        import aws_sdk_appsync.types.delta_sync_config

        out["deltaSyncConfig"] = aws_sdk_appsync.types.delta_sync_config.serialize_json(
            value["delta_sync_config"]
        )
    out["versioned"] = value.get("versioned", False)
    return out


def deserialize_json(data: dict) -> DynamodbDataSourceConfig:
    out: DynamodbDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("DynamodbDataSourceConfig.table_name required")
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    else:
        raise DeserializationError("DynamodbDataSourceConfig.aws_region required")
    if "useCallerCredentials" in data:
        out["use_caller_credentials"] = data["useCallerCredentials"]
    else:
        out["use_caller_credentials"] = False
    if "deltaSyncConfig" in data:
        import aws_sdk_appsync.types.delta_sync_config

        out["delta_sync_config"] = (
            aws_sdk_appsync.types.delta_sync_config.deserialize_json(
                data["deltaSyncConfig"]
            )
        )
    if "versioned" in data:
        out["versioned"] = data["versioned"]
    else:
        out["versioned"] = False
    return out
