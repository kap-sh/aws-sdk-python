"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentConstructsFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.list_network_migration_mapper_segment_construct_types_filter
    import aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter


class ListNetworkMigrationMapperSegmentConstructsFilters(TypedDict):
    construct_i_ds: NotRequired[
        "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter.ListNetworkMigrationMapperSegmentConstructsIDsFilter"
    ]
    """<p>A list of construct IDs to filter by.</p>"""
    construct_types: NotRequired[
        "aws_sdk_mgn.types.list_network_migration_mapper_segment_construct_types_filter.ListNetworkMigrationMapperSegmentConstructTypesFilter"
    ]
    """<p>A list of construct types to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentConstructsFilters) -> dict:
    out: dict = {}
    if "construct_i_ds" in value:
        import aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter

        out["constructIDs"] = (
            aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter.serialize_json(
                value["construct_i_ds"]
            )
        )
    if "construct_types" in value:
        import aws_sdk_mgn.types.list_network_migration_mapper_segment_construct_types_filter

        out["constructTypes"] = (
            aws_sdk_mgn.types.list_network_migration_mapper_segment_construct_types_filter.serialize_json(
                value["construct_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMapperSegmentConstructsFilters:
    out: ListNetworkMigrationMapperSegmentConstructsFilters = {}  # type: ignore[typeddict-item]
    if "constructIDs" in data:
        import aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter

        out["construct_i_ds"] = (
            aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter.deserialize_json(
                data["constructIDs"]
            )
        )
    if "constructTypes" in data:
        import aws_sdk_mgn.types.list_network_migration_mapper_segment_construct_types_filter

        out["construct_types"] = (
            aws_sdk_mgn.types.list_network_migration_mapper_segment_construct_types_filter.deserialize_json(
                data["constructTypes"]
            )
        )
    return out
