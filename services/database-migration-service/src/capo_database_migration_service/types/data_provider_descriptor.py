"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DataProviderDescriptor(TypedDict, closed=True):
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the Amazon Web Services Secrets Manager Secret used to store access credentials for the data provider.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the role used to access Amazon Web Services Secrets Manager.</p>"""
    data_provider_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The user-friendly name of the data provider.</p>"""
    data_provider_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the data provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderDescriptor) -> dict:
    out: dict = {}
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "data_provider_name" in value:
        out["DataProviderName"] = value["data_provider_name"]
    if "data_provider_arn" in value:
        out["DataProviderArn"] = value["data_provider_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataProviderDescriptor:
    out: DataProviderDescriptor = {}  # type: ignore[typeddict-item]
    if "SecretsManagerSecretId" in data:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if "SecretsManagerAccessRoleArn" in data:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if "DataProviderName" in data:
        out["data_provider_name"] = data["DataProviderName"]
    if "DataProviderArn" in data:
        out["data_provider_arn"] = data["DataProviderArn"]
    return out
