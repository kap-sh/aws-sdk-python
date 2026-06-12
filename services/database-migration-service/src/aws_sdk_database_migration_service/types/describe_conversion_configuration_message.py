"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeConversionConfigurationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project_identifier


class DescribeConversionConfigurationMessage(TypedDict):
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The name or Amazon Resource Name (ARN) for the schema conversion project to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConversionConfigurationMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConversionConfigurationMessage:
    out: DescribeConversionConfigurationMessage = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "DescribeConversionConfigurationMessage.migration_project_identifier required"
        )
    return out
