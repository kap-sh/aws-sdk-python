"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelChildrenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.metadata_model_reference_list
    import capo_database_migration_service.types.string


class DescribeMetadataModelChildrenResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of metadata model children. If a marker is returned, there are more metadata model children available.</p>"""
    metadata_model_children: NotRequired[
        "capo_database_migration_service.types.metadata_model_reference_list.MetadataModelReferenceList"
    ]
    """<p>A list of child metadata models.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelChildrenResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "metadata_model_children" in value:
        import capo_database_migration_service.types.metadata_model_reference_list

        out["MetadataModelChildren"] = (
            capo_database_migration_service.types.metadata_model_reference_list.serialize_aws_json_1_1(
                value["metadata_model_children"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelChildrenResponse:
    out: DescribeMetadataModelChildrenResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "MetadataModelChildren" in data:
        import capo_database_migration_service.types.metadata_model_reference_list

        out["metadata_model_children"] = (
            capo_database_migration_service.types.metadata_model_reference_list.deserialize_aws_json_1_1(
                data["MetadataModelChildren"]
            )
        )
    return out
