"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeConversionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DescribeConversionConfigurationResponse(TypedDict, closed=True):
    migration_project_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the schema conversion project.</p>"""
    conversion_configuration: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The configuration parameters for the schema conversion project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConversionConfigurationResponse) -> dict:
    out: dict = {}
    if "migration_project_identifier" in value:
        out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    if "conversion_configuration" in value:
        out["ConversionConfiguration"] = value["conversion_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConversionConfigurationResponse:
    out: DescribeConversionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    if "ConversionConfiguration" in data:
        out["conversion_configuration"] = data["ConversionConfiguration"]
    return out
