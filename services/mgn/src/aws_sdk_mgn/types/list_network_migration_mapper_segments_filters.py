"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.list_network_migration_mapper_segments_i_ds_filter


class ListNetworkMigrationMapperSegmentsFilters(TypedDict, closed=True):
    segment_i_ds: NotRequired[
        "aws_sdk_mgn.types.list_network_migration_mapper_segments_i_ds_filter.ListNetworkMigrationMapperSegmentsIDsFilter"
    ]
    """<p>A list of segment IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentsFilters) -> dict:
    out: dict = {}
    if "segment_i_ds" in value:
        import aws_sdk_mgn.types.list_network_migration_mapper_segments_i_ds_filter

        out["segmentIDs"] = (
            aws_sdk_mgn.types.list_network_migration_mapper_segments_i_ds_filter.serialize_json(
                value["segment_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMapperSegmentsFilters:
    out: ListNetworkMigrationMapperSegmentsFilters = {}  # type: ignore[typeddict-item]
    if "segmentIDs" in data:
        import aws_sdk_mgn.types.list_network_migration_mapper_segments_i_ds_filter

        out["segment_i_ds"] = (
            aws_sdk_mgn.types.list_network_migration_mapper_segments_i_ds_filter.deserialize_json(
                data["segmentIDs"]
            )
        )
    return out
