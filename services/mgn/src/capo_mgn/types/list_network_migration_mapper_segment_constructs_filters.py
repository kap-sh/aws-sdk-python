"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentConstructsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_mapper_segment_construct_types_filter
    import capo_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter


class ListNetworkMigrationMapperSegmentConstructsFilters(TypedDict, closed=True):
    construct_i_ds: NotRequired[
        "capo_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter.ListNetworkMigrationMapperSegmentConstructsIDsFilter"
    ]
    """<p>A list of construct IDs to filter by.</p>"""
    construct_types: NotRequired[
        "capo_mgn.types.list_network_migration_mapper_segment_construct_types_filter.ListNetworkMigrationMapperSegmentConstructTypesFilter"
    ]
    """<p>A list of construct types to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentConstructsFilters) -> dict:
    out: dict = {}
    if "construct_i_ds" in value:
        import capo_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter

        out["constructIDs"] = (
            capo_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter.serialize_json(
                value["construct_i_ds"]
            )
        )
    if "construct_types" in value:
        import capo_mgn.types.list_network_migration_mapper_segment_construct_types_filter

        out["constructTypes"] = (
            capo_mgn.types.list_network_migration_mapper_segment_construct_types_filter.serialize_json(
                value["construct_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMapperSegmentConstructsFilters:
    out: ListNetworkMigrationMapperSegmentConstructsFilters = {}  # type: ignore[typeddict-item]
    if "constructIDs" in data:
        import capo_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter

        out["construct_i_ds"] = (
            capo_mgn.types.list_network_migration_mapper_segment_constructs_i_ds_filter.deserialize_json(
                data["constructIDs"]
            )
        )
    if "constructTypes" in data:
        import capo_mgn.types.list_network_migration_mapper_segment_construct_types_filter

        out["construct_types"] = (
            capo_mgn.types.list_network_migration_mapper_segment_construct_types_filter.deserialize_json(
                data["constructTypes"]
            )
        )
    return out
