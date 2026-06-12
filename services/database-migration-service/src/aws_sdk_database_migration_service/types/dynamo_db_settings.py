"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DynamoDbSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DynamoDbSettings(TypedDict):
    service_access_role_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p> The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the <code>iam:PassRole</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDbSettings) -> dict:
    out: dict = {}
    out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDbSettings:
    out: DynamoDbSettings = {}  # type: ignore[typeddict-item]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    else:
        raise DeserializationError("DynamoDbSettings.service_access_role_arn required")
    return out
