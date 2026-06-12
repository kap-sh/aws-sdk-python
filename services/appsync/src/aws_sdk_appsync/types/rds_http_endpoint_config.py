"""Generated from Smithy shape ``com.amazonaws.appsync#RdsHttpEndpointConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class RdsHttpEndpointConfig(TypedDict):
    aws_region: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Amazon Web Services Region for Amazon RDS HTTP endpoint.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Amazon RDS cluster Amazon Resource Name (ARN).</p>"""
    database_name: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Logical database name.</p>"""
    schema: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Logical schema name.</p>"""
    aws_secret_store_arn: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>Amazon Web Services secret store Amazon Resource Name (ARN) for database credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsHttpEndpointConfig) -> dict:
    out: dict = {}
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "db_cluster_identifier" in value:
        out["dbClusterIdentifier"] = value["db_cluster_identifier"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "schema" in value:
        out["schema"] = value["schema"]
    if "aws_secret_store_arn" in value:
        out["awsSecretStoreArn"] = value["aws_secret_store_arn"]
    return out


def deserialize_json(data: dict) -> RdsHttpEndpointConfig:
    out: RdsHttpEndpointConfig = {}  # type: ignore[typeddict-item]
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    if "dbClusterIdentifier" in data:
        out["db_cluster_identifier"] = data["dbClusterIdentifier"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "schema" in data:
        out["schema"] = data["schema"]
    if "awsSecretStoreArn" in data:
        out["aws_secret_store_arn"] = data["awsSecretStoreArn"]
    return out
