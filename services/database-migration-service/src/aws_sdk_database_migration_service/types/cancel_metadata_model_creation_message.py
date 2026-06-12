"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelMetadataModelCreationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.string


class CancelMetadataModelCreationMessage(TypedDict):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    request_identifier: "aws_sdk_database_migration_service.types.string.String"
    """<p>The identifier for the metadata model creation operation to cancel. This operation was initiated by <code>StartMetadataModelCreation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMetadataModelCreationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["RequestIdentifier"] = value["request_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMetadataModelCreationMessage:
    out: CancelMetadataModelCreationMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "CancelMetadataModelCreationMessage.migration_project_identifier required"
        )
    if "RequestIdentifier" in data:
        out["request_identifier"] = data["RequestIdentifier"]
    else:
        raise DeserializationError(
            "CancelMetadataModelCreationMessage.request_identifier required"
        )
    return out
