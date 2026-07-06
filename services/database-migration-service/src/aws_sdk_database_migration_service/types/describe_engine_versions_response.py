"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEngineVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.engine_version_list
    import aws_sdk_database_migration_service.types.string


class DescribeEngineVersionsResponse(TypedDict, closed=True):
    engine_versions: NotRequired[
        "aws_sdk_database_migration_service.types.engine_version_list.EngineVersionList"
    ]
    """<p>Returned <code>EngineVersion</code> objects that describe the replication instance engine versions used in the project.</p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngineVersionsResponse) -> dict:
    out: dict = {}
    if "engine_versions" in value:
        import aws_sdk_database_migration_service.types.engine_version_list

        out["EngineVersions"] = (
            aws_sdk_database_migration_service.types.engine_version_list.serialize_aws_json_1_1(
                value["engine_versions"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngineVersionsResponse:
    out: DescribeEngineVersionsResponse = {}  # type: ignore[typeddict-item]
    if "EngineVersions" in data:
        import aws_sdk_database_migration_service.types.engine_version_list

        out["engine_versions"] = (
            aws_sdk_database_migration_service.types.engine_version_list.deserialize_aws_json_1_1(
                data["EngineVersions"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
