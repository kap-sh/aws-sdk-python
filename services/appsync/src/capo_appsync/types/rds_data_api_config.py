"""Generated from Smithy shape ``com.amazonaws.appsync#RdsDataApiConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.rds_data_api_config_database_name
    import capo_appsync.types.rds_data_api_config_resource_arn
    import capo_appsync.types.rds_data_api_config_secret_arn


class RdsDataApiConfig(TypedDict, closed=True):
    resource_arn: "capo_appsync.types.rds_data_api_config_resource_arn.RdsDataApiConfigResourceArn"
    """<p>The resource ARN of the RDS cluster.</p>"""
    secret_arn: (
        "capo_appsync.types.rds_data_api_config_secret_arn.RdsDataApiConfigSecretArn"
    )
    """<p>The secret's ARN that was obtained from Secrets Manager. A secret consists of secret information, the secret value, plus metadata about the secret. A secret value can be a string or binary. It typically includes the ARN, secret name and description, policies, tags, encryption key from the Key Management Service, and key rotation data.</p>"""
    database_name: "capo_appsync.types.rds_data_api_config_database_name.RdsDataApiConfigDatabaseName"
    """<p>The name of the database in the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDataApiConfig) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> RdsDataApiConfig:
    out: RdsDataApiConfig = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("RdsDataApiConfig.resource_arn required")
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("RdsDataApiConfig.secret_arn required")
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("RdsDataApiConfig.database_name required")
    return out
