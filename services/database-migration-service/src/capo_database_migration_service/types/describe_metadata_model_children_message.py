"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelChildrenMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.origin_type_value
    import capo_database_migration_service.types.string


class DescribeMetadataModelChildrenMessage(TypedDict, closed=True):
    selection_rules: "capo_database_migration_service.types.string.String"
    r"""<p>The JSON string that specifies which metadata model's children to retrieve. Only one selection rule with \"rule-action\": \"explicit\" can be provided. For more information, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Selections.html\">Selection Rules</a> in the DMS User Guide.</p>"""
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE | TARGET</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that indicates where the next page should start. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of metadata model children to include in the response. If more items exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelChildrenMessage) -> dict:
    out: dict = {}
    out["SelectionRules"] = value["selection_rules"]
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    import capo_database_migration_service.types.origin_type_value

    out["Origin"] = (
        capo_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelChildrenMessage:
    out: DescribeMetadataModelChildrenMessage = {}  # type: ignore[typeddict-item]
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "DescribeMetadataModelChildrenMessage.selection_rules required"
        )
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "DescribeMetadataModelChildrenMessage.migration_project_identifier required"
        )
    if "Origin" in data:
        import capo_database_migration_service.types.origin_type_value

        out["origin"] = (
            capo_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeMetadataModelChildrenMessage.origin required"
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    return out
