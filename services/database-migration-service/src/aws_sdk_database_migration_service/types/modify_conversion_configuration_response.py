"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyConversionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class ModifyConversionConfigurationResponse(TypedDict, closed=True):
    migration_project_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the modified configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyConversionConfigurationResponse) -> dict:
    out: dict = {}
    if "migration_project_identifier" in value:
        out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyConversionConfigurationResponse:
    out: ModifyConversionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    return out
