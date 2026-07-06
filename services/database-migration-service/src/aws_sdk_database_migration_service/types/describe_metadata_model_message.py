"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project_identifier
    import aws_sdk_database_migration_service.types.origin_type_value
    import aws_sdk_database_migration_service.types.string


class DescribeMetadataModelMessage(TypedDict, closed=True):
    selection_rules: "aws_sdk_database_migration_service.types.string.String"
    r"""<p>The JSON string that specifies which metadata model to retrieve. Only one selection rule with \"rule-action\": \"explicit\" can be provided. For more information, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Selections.html\">Selection Rules</a> in the DMS User Guide.</p>"""
    migration_project_identifier: "aws_sdk_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    origin: "aws_sdk_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE | TARGET</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelMessage) -> dict:
    out: dict = {}
    out["SelectionRules"] = value["selection_rules"]
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    import aws_sdk_database_migration_service.types.origin_type_value

    out["Origin"] = (
        aws_sdk_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelMessage:
    out: DescribeMetadataModelMessage = {}  # type: ignore[typeddict-item]
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "DescribeMetadataModelMessage.selection_rules required"
        )
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "DescribeMetadataModelMessage.migration_project_identifier required"
        )
    if "Origin" in data:
        import aws_sdk_database_migration_service.types.origin_type_value

        out["origin"] = (
            aws_sdk_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError("DescribeMetadataModelMessage.origin required")
    return out
